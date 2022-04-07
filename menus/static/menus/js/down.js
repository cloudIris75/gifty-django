const wrap = document.getElementById('wrap');
const button = document.getElementById('down');

button.onclick = function() {
    wrap.scroll({
        top: wrap.scrollHeight,
        left: 0,
        behavior: 'smooth'
    });
};