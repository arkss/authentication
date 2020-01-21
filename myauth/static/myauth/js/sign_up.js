window.onload = () => {
    const inputUsername = document.getElementById("username");
    const inputPassword = document.getElementById("password");
    const inputCheckPassword = document.getElementById("check_password");
    const inputEmail = document.getElementById("email");
    const signUpForm = document.getElementById('sign_up_form');
    const fakeSubmit = document.getElementById('fake_submit');

    fakeSubmit.addEventListener('click', signUpSubmit);

    function signUpSubmit() {
        const isValid = validationCheck();
        if (!isValid) return;

        fetch('http://localhost:8000/sign_up/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user: {
                    username: inputUsername.value,
                    password: inputPassword.value,
                    email: inputEmail.value
                }
            })
        }).then(result => {
            return result.json()
        }).then(data => {
            if (data.response == "success"){
                alert("회원가입 성공!");
                location.href = "http://localhost:8000/login/"
            } else {
                alert("회원가입 실패!");
            }
        }).catch(e=>{
            console.log(e);
        });
    };

    function validationCheck() {
        if ($(".username_input").attr("check_result") === "fail") {
            alert("아이디 중복체크를 해주시기 바랍니다.");
            $(".username_input").focus();
            return false;
        }

        if (inputPassword.value != inputCheckPassword.value) {
            alert("비밀번호가 일치하지 않습니다.");
            document.querySelector('input[name="password1"]').focus();
            return false;
        }
        return true;
    }
}



// function lawyerSubmit() {
//     // 제출 시, 아이디 중복체크가 되지않았으면 오류 알람 띄우기
//     if ($(".username_input").attr("check_result") === "fail") {
//         alert("아이디 중복체크를 해주시기 바랍니다.");
//         $(".username_input").focus();
//         return false;
//     }

//     // 비밀번호와 비밀번호 확인이 일치하는지 확인
//     password1 = document.querySelector('input[name="password1"]').value
//     password2 = document.querySelector('input[name="password2"]').value

//     if (password1 != password2) {
//         alert("비밀번호가 일치하지 않습니다.");
//         document.querySelector('input[name="password1"]').focus();
//         return;
//     }

//     // js submit 은 required 가 실행이 안되서 다음과 같이 button을 클릭하도록
//     document.querySelector("#real_submit").click();
// }

// const fakeSubmit = document.getElementById('fake_submit');

// fakeSubmit.addEventListener('click', lawyerSubmit);