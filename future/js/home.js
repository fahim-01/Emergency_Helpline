const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelector(".nav-links li");

hamburger.addEventListener('çlick', () => {
  navLinks.classList.toggle("open"); 
});