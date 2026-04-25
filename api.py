from threading import Lock

from flask import Flask, jsonify, request

from TIA_wrapper import TIA_wrapper


app = Flask(__name__)

_tia_wrapper = None
_tia_lock = Lock()


def get_tia_wrapper() -> TIA_wrapper:
    global _tia_wrapper
    if _tia_wrapper is None:
        with _tia_lock:
            if _tia_wrapper is None:
                _tia_wrapper = TIA_wrapper()
    return _tia_wrapper


@app.get("/api")
def root():
    return jsonify(
        {
            "name": "TIA API",
            "endpoints": {
                "projects": "/api/projects",
                "plcs": "/api/projects/<project_name>/plcs",
                "blocks": "/api/projects/<project_name>/plcs/<plc_name>/blocks",
                "block_code": "/api/projects/<project_name>/plcs/<plc_name>/blocks/<block_name>/code",
            },
        }
    )


@app.get("/api/projects")
def list_projects():
    try:
        projects = get_tia_wrapper().list_projects()
        return jsonify({"projects": projects})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.get("/api/projects/<path:project_name>/plcs")
def list_plcs(project_name):
    try:
        plcs = get_tia_wrapper().list_plcs(project_name)
        return jsonify({"project": project_name, "plcs": plcs})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.get("/api/projects/<path:project_name>/plcs/<path:plc_name>/blocks")
def list_program_blocks(project_name, plc_name):
    try:
        blocks = get_tia_wrapper().list_SCL_blocks(project_name, plc_name)
        return jsonify({"project": project_name, "plc": plc_name, "blocks": blocks})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.get("/api/projects/<path:project_name>/plcs/<path:plc_name>/blocks/<path:block_name>/code")
def get_program_block_code(project_name, plc_name, block_name):
	try:
		code = get_tia_wrapper().get_code(project_name, plc_name, block_name)
		return jsonify(
			{
				"project": project_name,
				"plc": plc_name,
				"block": block_name,
				"code": code,
			}
		)
	except Exception as exc:
		return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
