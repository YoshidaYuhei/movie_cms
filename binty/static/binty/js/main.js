$('.search-button').on('click', function(){

    $('.search-box').css('visibility', 'visible');
    $('.nav-item').css('visibility', 'hidden');

});


$('.test-button').on('click', function(){
    $('.blurry-menu').css('border', '2px solid red').add('p').css('background', 'red');
});


$('.subform').on('click', function(){
    var btn = this.value;
    var url = 'subform' + '?btn=' + btn;
    window.open(url, 'subform', "top=50,left=50,width=500,height=500,scrollbars=1,location=0,menubar=0,toolbar=0,status=1,directories=0,resizable=1");
    return false;
});
