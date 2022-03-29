const url = window.location.pathname;
const links = document.getElementsByClassName('link');

if (url.includes('brands')) {
    links[1].classList.toggle('active');
} else if (url.includes('menus')) {
    links[2].classList.toggle('active');
} else if (url.includes('calculator')) {
    links[3].classList.toggle('active');
} else {
    links[0].classList.toggle('active');
}
