const wrap = document.getElementById('wrap');
const button = document.getElementById('down');

button.onclick = function() {
    wrap.scroll({
        top: wrap.scrollHeight,
        left: 0,
        behavior: 'smooth'
    });
};

function view() {
    document.getElementById('message').classList.toggle('active');
};