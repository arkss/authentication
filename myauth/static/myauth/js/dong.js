window.onload = () =>{
    const inputEmail = document.getElementById('email');
    const inputPasswword = document.getElementById('password')
    const loginForm = document.getElementById('formLogin');

    init();

    function init(){

        loginForm.addEventListener('submit',()=>{
            fetch('/users/login',{
                method:'POST',
                headers:{
                    'Content-Type' : 'application/json'
                },
                body : JSON.stringify({
                    email : inputEmail.value,
                    password : inputPasswword.value
                })
            }).then(result=>{
                return result.json()
            }).then(data=>{
                if(data.msg==="success"){
                    alert("로그인 성공!");
                    location.href ='/front/';
                }else{
                    alert("로그인 실패!");
                }
            }).catch(err=>{
                console.log(err);
            });
        });

    }

};

/*
데이터 example
users/create/

<request>
{
    "user": {
        "username": "rkdalstjd9",
        "password": "qwe123",
        "first_name": "minsung",
        "last_name": "kang"
    }
}

{
    "user": {
        "username": "rkdalstjd9",
        "password": "qwe123"
    }
}

<response>
{
    "response": "success",
    "message": "user create sucessfully"
}

token-auth/
<request>
{
    "username": "rkdalstjd9",
    "password": "qwe123"
}

<response>
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InJrZGFsc3RqZDkiLCJleHAiOjE1Nzk1ODE0NDQsImVtYWlsIjoiIn0.WpzOLt_25ZRva4vWQ0omh70ZjojHgciBX9LjlPYleQo",
    "user": {
        "id": 3,
        "username": "rkdalstjd9",
        "is_superuser": false,
        "first_name": "minsung",
        "last_name": "kang"
    }
}


*/