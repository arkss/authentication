window.onload = () => {
    const inputUsername = document.getElementById("username");
    const inputPassword = document.getElementById("password");
    const loginForm = document.getElementById("login_form");

    loginSubmit();

    function loginSubmit(){
        loginForm.addEventListener('submit', ()=>{
            fetch('http://localhost:8000/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
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
                console.log(data);
                if (data.response == "success"){
                    alert("로그인 성공!");
                    location.href = "http://localhost:8000/main/"
                } else {
                    alert("로그인 실패!");
                }
            }).catch(e=>{
                console.log(e);
            });
            event.preventDefault();
        })
    };
}
