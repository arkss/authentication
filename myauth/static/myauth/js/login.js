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
                if (data.response == "success"){
                    // setCookie('jwttoken', data['jwt_token'], 3)
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

function setCookie(cookie_name, value, days){
    alert("setCookie");
    var exdate = new Date();
    exdate.setDate(exdate.getDate()+days);
    var cookie_value = escape(value) + ((days == null) ? '' : ';    expires=' + exdate.toUTCString());
    document.cookie = cookie_name+'='+cookie_value;
}

function getCookie(cookie_name) {
    var x, y;
    var val = document.cookie.split(';');
  
    for (var i = 0; i < val.length; i++) {
      x = val[i].substr(0, val[i].indexOf('='));
      y = val[i].substr(val[i].indexOf('=') + 1);
      x = x.replace(/^\s+|\s+$/g, ''); // 앞과 뒤의 공백 제거하기
      if (x == cookie_name) {
        return unescape(y); // unescape로 디코딩 후 값 리턴
      }
    }
  }