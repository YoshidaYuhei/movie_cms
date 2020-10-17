// csrf_tokenの取得に使う
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Ajaxの実装
$(function () {
    $('.goodbtn').click(function () {
        var usrname = $("#username").text()  // いいねしたユーザid
        var Cntid = $(this).attr('id') // 対象コンテンツid
        $.ajax({
            type: 'POST',
            url: 'ajax/',
            data: {'btn_id': Cntid, 'usrname': usrname},
            // dataType: 'json',
            // contentType: "application/json",
            beforeSend: function(xhr, settings){
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }).done(function (res) {
            tagid = "#like_span_" + res.cntid
            num = "(" + res.count + ")"
            $(tagid).text(num);

        }).fail(function (data) {
            console.log('error')
        })
    })
});
