function changeOrder(select) {
    var orderSelect = select.options[select.selectedIndex].value;
    var list = '';
    var ul = '';

    switch (orderSelect) {
        case 'order':
        case 'name':
            list = 'menu_name';
            break;
        case 'descending':
            list = 'menu_descending';
            break;
        case 'ascending':
            list = 'menu_ascending';
            break;
    }

    ul = `{% if ` + list + ` %}
            <ul class="list">
                {% for menu in ` + list + ` %}
                    <li>
                        <div class="item">
                            <img class="image" src={% get_static_prefix %}{{menu.img_path}}>
                            <h3 class="name">{{menu.name}}</h3>
                            <h3 class="price">{{menu.price|intcomma}}원</h3>
                        </div>
                    </li>
                {% endfor %}
            </ul>
        {% endif %}`;

    document.getElementById('menu-list').innerHTML = ul;
}