let ImageCodeId = '';

function generate_UUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        let r = Math.random() * 16 | 0,
            v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}
function generate_ImageCodeId() {
    ImageCodeId = generate_UUID();
    let url = '/image?img_id=' + ImageCodeId;
    $('.check').attr('src', url)
}

$(function () {
    generate_ImageCodeId();
});


