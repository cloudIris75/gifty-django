window.onload = function info() {
    let gifticon = document.getElementById('gifticon-price').innerHTML;
    let gifticon_int = parseInt(gifticon.replace('원', '').replace(',', ''), 10);

    let menu1 = document.getElementById('menu1-price').innerHTML;
    let menu1_int = parseInt(menu1.replace('원', '').replace(',', ''), 10);
    let menu2 = document.getElementById('menu2-price').innerHTML;
    let menu2_int = parseInt(menu2.replace('원', '').replace(',', ''), 10);

    let price_int = menu1_int + menu2_int;
    let differ = Math.abs(gifticon_int - menu1_int - menu2_int).toLocaleString();
    let result = document.getElementById('result');

    if (price_int < gifticon_int) {
        result.innerHTML += `기프티콘 가격보다 ` + differ + `원 부족해요! <br>`
        + differ + `원 어치 추가 선택해주세요.`;
    } else if (price_int > gifticon_int) {
        result.innerHTML += `기프티콘 가격보다 ` + differ + `원 많아요! <br>`
        + differ + `원 차액 결제해주세요.`;
    } else {
        result.innerHTML += `기프티콘 가격과 동일해요! <br>
        바로 결제해주세요.`;
    }
}