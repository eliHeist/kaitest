// header
let lastScroll = 0;
const nav = document.getElementById("navbar-sticky");
document.getElementById("hero-space").style.height = nav.offsetHeight + "px";

window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
        nav.classList.remove("show");
    }
    if (currentScroll > lastScroll && !nav.classList.contains("hidden")) {
        nav.classList.remove("show");
        nav.classList.add("hidden");
    }
    if (currentScroll < lastScroll && nav.classList.contains("hidden")) {
        nav.classList.remove("hidden");
        nav.classList.add("show");
    }
    lastScroll = currentScroll;
});