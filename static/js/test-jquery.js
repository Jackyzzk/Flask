// $代表jQuery对象，同时也是一个函数对象
// $()和jQuery()是jQuery的核心函数，执行这两个元素返回的是一个DOM元素
// 文档对象模型（Document Object Model，简称DOM）
// $()是一个函数，等同于jQuery()，可在括号内传参数，传参后可获取元素

// window.onload = function () {
//     alert('原生js hello');
// };
//
// $(document).ready(function () {
//     alert('jquery ready');
// });

$(function () {
    // alert('简化ready');

    let $div1 = $('#01');
    $div1.css({'color': 'red', 'font-size': 20});
    // alert($div1.css('font-size'));

    let $input = $('.input');

    $input.css({'color': 'orange'});

    // $input.click(function () {
    //     // this.style.background = 'yellow';  // 原生js
    //     $(this).css({'background': 'yellow'});
    //     });

    $input.mouseover(function (event) {
        // 只有数字值可创建动画（比如 "margin:30px"）。字符串值无法创建动画（比如 "background-color:red"）。
        $(this).animate({'font-size': 30});
        event.stopPropagation();
        event.preventDefault();
    });
    $input.mouseout(function (event) {
        $(this).animate({'font-size': 20});
        return false;  // 阻止事件冒泡？？
    });

    // 为何不行？
    $input.delegate('des', 'click', function () {
        $(this).css({'color': 'red'});
    });

    // $.ajax() 返回其创建的 XMLHttpRequest 对象。用于执行 AJAX（异步 HTTP）请求。
    $.ajax({
        url: 'data/data.txt',
        type: 'get',
        dataType: 'text',
        success: function (ret) {
            // alert(ret);
            // 千万不要在文档加载后使用 document.write()。这么做会覆盖文档。提前预置好新标签。
            $('data').html(ret);
        }, 
        error: function () {
            alert('error');
        }
    })


});

// JavaScript对象 Json
// JavaScript Object Notation
