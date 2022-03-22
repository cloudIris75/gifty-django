window.onload = function info() {
    let gifticon, menu1, menu2, menu3, menu4, menu5, result, differ = '';
    let gifticon_int, menu1_int, menu2_int, menu3_int, menu4_int, menu5_int, price_int = 0;

    if (document.getElementById('gifticon-price')) {
        gifticon = document.getElementById('gifticon-price').innerHTML;
        gifticon_int = parseInt(gifticon.replace('원', '').replace(',', ''), 10);

        if (document.getElementById('menu1-price')) {
            menu1 = document.getElementById('menu1-price').innerHTML;
            menu1_int = parseInt(menu1.replace('원', '').replace(',', ''), 10);
            price_int += menu1_int;
        }
        if (document.getElementById('menu2-price')) {
            menu2 = document.getElementById('menu2-price').innerHTML;
            menu2_int = parseInt(menu2.replace('원', '').replace(',', ''), 10);
            price_int += menu2_int;
        }
        if (document.getElementById('menu3-price')) {
            menu3 = document.getElementById('menu3-price').innerHTML;
            menu3_int = parseInt(menu3.replace('원', '').replace(',', ''), 10);
            price_int += menu3_int;
        }
        if (document.getElementById('menu4-price')) {
            menu4 = document.getElementById('menu4-price').innerHTML;
            menu4_int = parseInt(menu4.replace('원', '').replace(',', ''), 10);
            price_int += menu4_int;
        }
        if (document.getElementById('menu5-price')) {
            menu5 = document.getElementById('menu5-price').innerHTML;
            menu5_int = parseInt(menu5.replace('원', '').replace(',', ''), 10);
            price_int += menu5_int;
        }

        differ = Math.abs(gifticon_int - price_int).toLocaleString();
    }
    
    if (document.getElementById('result')) {
        result = document.getElementById('result');

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
}
