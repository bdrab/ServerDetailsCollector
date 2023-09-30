let homeImg = document.querySelector(".home-img")
let loadingDiv = document.querySelector(".loading-div")
let loginDiv = document.querySelector(".login-div")
let loginBtn = document.querySelector(".login-submit-btn")



homeImg.addEventListener("click", e => {
    homeImg.classList.toggle("hide");
    loadingDiv.classList.toggle("hide");
    setTimeout(() => {
        loadingDiv.classList.toggle("hide");
        loginDiv.classList.toggle("hide");
    }, 100);
})


loginBtn.addEventListener("click", e => {
    loginDiv.classList.toggle("hide");
    loadingDiv.classList.toggle("hide");
})


