function removeClass() {
    if (document.getElementById('menu5').classList.contains('active')) {
        document.getElementById('menu5').classList.remove('active');
    } else if (document.getElementById('menu4').classList.contains('active')) {
        document.getElementById('menu4').classList.remove('active');
    } else if (document.getElementById('menu3').classList.contains('active')) {
        document.getElementById('menu3').classList.remove('active');
    } else if (document.getElementById('menu2').classList.contains('active')) {
        document.getElementById('menu2').classList.remove('active');
    }
}

function addClass() {
    if (!document.getElementById('menu2').classList.contains('active')) {
        document.getElementById('menu2').classList.add('active');
    } else if (!document.getElementById('menu3').classList.contains('active')) {
        document.getElementById('menu3').classList.add('active');
    } else if (!document.getElementById('menu4').classList.contains('active')) {
        document.getElementById('menu4').classList.add('active');
    } else if (!document.getElementById('menu5').classList.contains('active')) {
        document.getElementById('menu5').classList.add('active');
    }
}
