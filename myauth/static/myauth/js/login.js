window.onload = () => {
    const inputUsername = document.getElementById("username");
    const inputPassword = document.getElementById("password");
    const loginForm = document.getElementById("login_form");
    const inputcsrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]');

    loginSubmit();

    function loginSubmit() {
        loginForm.addEventListener('submit', () => {
            fetch('http://localhost:8000/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': inputcsrfToken.value
                },
                body: JSON.stringify({
                    user: {
                        username: inputUsername.value,
                        password: inputPassword.value
                    }
                })
            }).then(result => {
                return result.json()
            }).then(data => {
                if (data.response == "success") {
                    // setCookie('jwttoken', data['jwt_token'], 3)
                    alert("로그인 성공!");
                    location.href = "http://localhost:8000/main/"
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