const html = document.getElementById('html');
const button = document.getElementById('down');

if (button) {
    button.onclick = function() {
        html.scroll({
            top: html.scrollHeight,
            left: 0,
            behavior: 'smooth'
        });
    };
}

function view() {
    document.getElementById('message').classList.toggle('active');
};