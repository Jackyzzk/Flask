function ajax1() {
    let data = {'name': $('#01').val()};
    $.post({
        url: '/ajax1',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (res) {
            $('#info-1').html(res.name)  // 返回的res是一个Json格式的对象，取值相当于获取对象属性
        }
    })
}

function ajax2() {
    let data = {'pwd': $('#02').val()};
    $.post({
        url: '/ajax2',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (res) {
            $('#info-2').html(res.pwd)  // 返回的res是一个Json格式的对象，取值相当于获取对象属性
        }
    })
}

function ajax3() {
    let data = {'page': $('#03').val()};
    $.post({
        url: '/ajax3',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (res) {
            $('#info-3').html(res.page);  // 返回的res是一个Json格式的对象，取值相当于获取对象属性
            $('#04').attr('src', 'https://' + res.page);
        }
    })
}

// 使用简写 $.post() 时，默认的 contentType 不是 application/json，也无法更改
