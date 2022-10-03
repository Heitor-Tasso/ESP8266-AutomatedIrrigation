
$(document).ready(function () {
    /*
    fazer um icon ter comportamento de ToggleButton.
    simula o olho do input de senha para esconder a senha.
    */
    $('.show-eye-icon').click(function () {
        let input = $('.input-password input')[0];
        $(this).toggleClass("down");
        
        if (input.getAttribute('type') == 'password') {
            input.setAttribute('type', 'text');
            $(this)[0].setAttribute('src', 'assets/eye-out.png');
        }
        else {
            input.setAttribute('type', 'password');
            $(this)[0].setAttribute('src', 'assets/eye-off-out.png');
        }
    });

});
