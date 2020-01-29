window.onload = () => {
    const inputPassword = document.getElementById("password")
    const inputCheckPassword = document.getElementById("check_password")
    const changePasswordForm = document.getElementById("login_form");

    changePasswordSubmit();

    function changePasswordSubmit() {
        changePasswordForm.addEventListener('submit', () => {

            fetch('http://localhost:8000/change_password/' + uuid + '/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    password: inputPassword.value,
                    check_password: inputCheckPassword.value
                })
            }).then(result => {
                console.log(result)
                return result.json()
            }).then(data => {
                console.log(data)
                if (data.response == "success") {
                    alert(data.message);
                    location.href = "http://localhost:8000/login/"
                } else {
                    console.log(data.message);
                    alert(data.message);
                }
            }).catch(e => {
                console.log(e);
            });
            event.preventDefault();
        })
    };
}


