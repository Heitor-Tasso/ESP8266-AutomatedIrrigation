
document.getElementsByClassName('show-eye-icon')[0].onclick = function () {
    let input = document.getElementsByClassName('input-password')[0].getElementsByTagName("input")[0];
    console.log(input);
    console.log(this);
    this.classList.toggle("down");
    
    if (input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
        this.setAttribute('src', 'assets/eye-out.png');
    }
    else {
        input.setAttribute('type', 'password');
        this.setAttribute('src', 'assets/eye-off-out.png');
    }
};
