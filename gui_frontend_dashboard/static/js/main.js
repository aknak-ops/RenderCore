function loadSummary() {
    fetch("/summary")
        .then(response => response.json())
        .then(data => {
            let box = document.getElementById("summaryBox");
            if (data.error) {
                box.innerHTML = "<p>" + data.error + "</p>";
            } else {
                box.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
            }
        });
}

function runRender() {
    alert("Triggering render... (hook up render script)");
}