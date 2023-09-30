let pageContent = document.querySelector(".table-div")
let addDeviceBtn = document.querySelector("#add-device-btn")
let addDeviceDiv = document.querySelector(".add-device-div")
let closeModalBtn = document.querySelector(".close-modal-div-btn")
let submitBtn = document.querySelector(".add-device-btn-submit")



closeModalBtn.addEventListener("click", e => {
    addDeviceDiv.classList.add("hide");
    document.querySelector(".table-div").style.filter = "";
})


addDeviceBtn.addEventListener("click", e =>{
    addDeviceDiv.classList.remove("hide");
    document.querySelector(".table-div").style.filter = "blur(8px)";
})


submitBtn.addEventListener("click", async (event) => {
    let data = new FormData()
    let hostname = document.querySelector("#device-hostname").value
    let ip = document.querySelector("#device-ip").value
    let port = document.querySelector("#device-port").value

    data.append('hostname', hostname)
    data.append('ip', ip)
    data.append('port', port)

    let response = await fetch('http://127.0.0.1:8000/device/add', {
                    method: "POST",
                    headers: {'X-CSRFToken': csrftoken},
                    body: data
                    });
    responseData = await response;
    responseStatus = await response.status;
    if(responseStatus === 204){
        location.reload();
    }
})