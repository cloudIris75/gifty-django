function counter(type) {
    let count = document.getElementById('gifticon-count');
    let num = count.value;

    if (type === 'plus') {
        if (num < 5) {
            num++;
        }
    } else if (type === 'minus') {
        if (num > 1) {
            num--;
        }
    }

    count.value = num;
}