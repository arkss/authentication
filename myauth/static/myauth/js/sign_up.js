window.onload = () => {
    const inputUsername = document.getElementById("username");
    const inputPassword = document.getElementById("password");
    const inputCheckPassword = document.getElementById("check_password");
    const inputEmail = document.getElementById("email");
    const signUpForm = document.getElementById('sign_up_form');
    const fakeSubmit = document.getElementById('fake_submit');
    const inputcsrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]');

    fakeSubmit.addEventListener('click', signUpSubmit);

    function signUpSubmit() {
        const isValid = validationCheck();
        if (!isValid) return;

        fetch('/sign_up/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': inputcsrfToken.value
            },
            body: JSON.stringify({
                user: {
                    username: inputUsername.value,
                    password: inputPassword.value,
                    email: inputEmail.value
                }
            })
        }).then(result => {
            // result.status : response status 확인
            console.log(result.status);
            return result.json()
        }).then(data => {
            if (data.response == "success") {
                alert("회원가입 성공!");
                location.href = "/login/"
            } else {
                alert(data.message);
            }
        }).catch(e => {
            console.log(e);
        });
    };

    function validationCheck() {
        if ($(".username_input").attr("check_result") === "fail") {
            alert("아이디 중복체크를 해주시기 바랍니다.");
            $(".username_input").focus();
            return false;
        }
        if (inputPassword.value.length < 8) {
            alert("비밀번호는 8자 이상으로 해주시기 바랍니다.");
            document.querySelector('input[name="password1"]').focus();
            return false;
        }

        if (inputPassword.value != inputCheckPassword.value) {
            alert("비밀번호가 일치하지 않습니다.");
            document.querySelector('input[name="password1"]').focus();
            return false;
        }

        const emailValidator = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (!emailValidator.test(inputEmail.value)) {
            alert("이메일이 유효하지 않습니다.");
            return false;
        }

        return true;
    }
}