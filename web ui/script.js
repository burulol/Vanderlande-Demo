
function onLoad() {
    // Create event listener for project selection

    const projectSelect = document.getElementById("project-select");

    projectSelect.addEventListener("change", (event) => {
        const selectedProject = event.target.value;
        const plcSelectElement = document.getElementById("plc-select");

        resetPlcSelect();

        if (selectedProject != "") {
            fetchPLCs(selectedProject);
            plcSelectElement.disabled = false;
        }
    });

    // Create event listener for PLC selection

    const plcSelect = document.getElementById("plc-select");

    plcSelect.addEventListener("change", (event) => {
        const selectedPLC = event.target.value;
        const blockSelectElement = document.getElementById("block-select");

        resetBlockSelect()

        if (selectedPLC != "") {
            const selectedProject = projectSelect.value;
            fetchBlocks(selectedProject, selectedPLC);
            blockSelectElement.disabled = false;
        }
    });

    // Create event listener for block selection

    const blockSelect = document.getElementById("block-select");

    blockSelect.addEventListener("change", (event) => {
        const selectedBlock = event.target.value;

        if (selectedBlock != "") {
            const selectedProject = projectSelect.value;
            const selectedPLC = plcSelect.value;
            fetch(`/api/projects/${encodeURIComponent(selectedProject)}/plcs/${encodeURIComponent(selectedPLC)}/blocks/${encodeURIComponent(selectedBlock)}/code`)
                .then(response => response.json())
                .then(data => {
                    populateCodeDisplay(data.code);
                })
        } else {
            resetCodeDisplay();
        }
    });
}

function loadReferenceCode() {
    const reference_code = "FUNCTION_BLOCK MotorControl\nVAR_INPUT\n    Enable : BOOL;\n    TargetSpeed : INT;\nEND_VAR\nVAR_OUTPUT\n    Running : BOOL;\n    Speed : INT;\nEND_VAR\n\nIF #Enable THEN\n    #Speed := #TargetSpeed;\n    #Running := TRUE;\nELSE\n    #Speed := 0;\n    #Running := FALSE;\nEND_IF;";

    const reference_code_element = document.getElementById("reference-code");
    reference_code_element.textContent = reference_code;
}

function populateProjectSelect(projects) {
    const projectSelectElement = document.getElementById("project-select");
    projectSelectElement.innerHTML = "";

    empty_option = document.createElement("option");
    empty_option.textContent = "-- Select a project --";
    empty_option.value = "";
    projectSelectElement.appendChild(empty_option);

    projects.forEach(project => {
        const option = document.createElement("option");
        option.textContent = project;
        option.value = project;
        projectSelectElement.appendChild(option);
    });
}

function populatePLCSelect(plcs) {

    const plcSelectElement = document.getElementById("plc-select");
    plcSelectElement.innerHTML = "";

    empty_option = document.createElement("option");
    empty_option.textContent = "-- Select a PLC --";
    empty_option.value = "";
    plcSelectElement.appendChild(empty_option);

    plcs.forEach(plc => {
        const option = document.createElement("option");
        option.textContent = plc;   
        option.value = plc;
        plcSelectElement.appendChild(option);
    });
}

function populateBlockSelect(blocks) {
    const blockSelectElement = document.getElementById("block-select");
    blockSelectElement.innerHTML = "";  
    
    empty_option = document.createElement("option");
    empty_option.textContent = "-- Select a block --";
    empty_option.value = "";
    blockSelectElement.appendChild(empty_option);

    blocks.forEach(block => {
        const option = document.createElement("option");
        option.textContent = block;   
        option.value = block;
        blockSelectElement.appendChild(option);
    });
}

function populateCodeDisplay(code) {
    const codeElement = document.getElementById("local-code");
    codeElement.textContent = code;

    document.getElementById('local-code-placeholder').style.display = 'none';
}

function resetPlcSelect() {
    const plcSelectElement = document.getElementById("plc-select");
    plcSelectElement.innerHTML = "";
    empty_option = document.createElement("option");
    empty_option.textContent = "-- Select a PLC --";
    empty_option.value = "";
    plcSelectElement.appendChild(empty_option);
    plcSelectElement.disabled = true;

    resetBlockSelect();
}

function resetBlockSelect() {
    const blockSelectElement = document.getElementById("block-select");
    blockSelectElement.innerHTML = "";
    empty_option = document.createElement("option");
    empty_option.textContent = "-- Select a block --";
    empty_option.value = "";
    blockSelectElement.appendChild(empty_option);
    blockSelectElement.disabled = true;

    resetCodeDisplay();
}

function resetCodeDisplay() {
    const codeElement = document.getElementById("local-code");
    codeElement.textContent = "";
    document.getElementById('local-code-placeholder').style.display = 'inline-block';
}

function fetchProjects() {
    fetch("/api/projects")
        .then(response => response.json())
        .then(data => {
            populateProjectSelect(data.projects);
        })
}

function fetchPLCs(projectName) {
    fetch(`/api/projects/${encodeURIComponent(projectName)}/plcs`)
        .then(response => response.json())
        .then(data => {
            populatePLCSelect(data.plcs);
        })
}

function fetchBlocks(projectName, plcName) {
    fetch(`/api/projects/${encodeURIComponent(projectName)}/plcs/${encodeURIComponent(plcName)}/blocks`)
        .then(response => response.json())
        .then(data => {
            populateBlockSelect(data.blocks);
        })
}

document.addEventListener("DOMContentLoaded", loadReferenceCode);
document.addEventListener("DOMContentLoaded", fetchProjects);
document.addEventListener("DOMContentLoaded", onLoad)


