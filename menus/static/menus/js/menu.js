function add() {
    if (!document.getElementById('menu2').style.display || document.getElementById('menu2').style.display == 'none') {
        document.getElementById('menu2').style.display = 'flex';
    } else if (!document.getElementById('menu3').style.display || document.getElementById('menu3').style.display == 'none') {
        document.getElementById('menu3').style.display = 'flex';
    } else if (!document.getElementById('menu4').style.display || document.getElementById('menu4').style.display == 'none') {
        document.getElementById('menu4').style.display = 'flex';
    } else if (!document.getElementById('menu5').style.display || document.getElementById('menu5').style.display == 'none') {
        document.getElementById('menu5').style.display = 'flex';
    }
    console.log(document.getElementById('menu2').style.display);
}

function remove() {
    if (document.getElementById('menu5').style.display == 'flex') {
        document.getElementById('menu5').style.display = 'none';
    } else if (document.getElementById('menu4').style.display == 'flex') {
        document.getElementById('menu4').style.display = 'none';
    } else if (document.getElementById('menu3').style.display == 'flex') {
        document.getElementById('menu3').style.display = 'none';
    } else if (document.getElementById('menu2').style.display == 'flex') {
        document.getElementById('menu2').style.display = 'none';
    }
}