function counter(type, item) {
    const form = document.getElementById('form');
    const count = document.getElementById(item);
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
    form.submit();
}
