const url = window.location.pathname;
const links = document.getElementsByClassName('link');

switch (url) {
    case '/':
        links[0].classList.toggle('active');
        break;
    case '/brands/':
        links[1].classList.toggle('active');
        break;
    case '/menus/':
        links[2].classList.toggle('active');
        break;
    case '/calculator/':
        links[3].classList.toggle('active');
        break;
}

