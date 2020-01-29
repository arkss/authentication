window.onload = () => {
    const inputUsername = document.getElementById("username");
    const findPasswordForm = document.getElementById("login_form");
    const inputcsrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]');

    findPasswordSubmit();

    function findPasswordSubmit() {
        findPasswordForm.addEventListener('submit', () => {
            fetch('http://localhost:8000/find_password/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRFToken': inputcsrfToken.value
                },
                body: JSON.stringify({
                    username: inputUsername.value,
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
