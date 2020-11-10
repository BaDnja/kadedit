const loginBtn = document.getElementById('login-btn');
const loginError = document.getElementById('login-error');


loginBtn.addEventListener("click", validateLogin);

function showError(text) {
  loginError.style.visibility = "visible";
  loginError.innerHTML = text;
  setTimeout(() => {
    loginError.style.visibility = "hidden";
  }, 2000);
}
function validateLogin(e) {
  const loginUsername = document.getElementById('login-username').value;
  const loginPassword = document.getElementById('login-password').value;
  if (loginUsername === "") {
    if(loginPassword === "") {
      showError("Niste unijeli ni korisničko ime ni šifru!");
    }
    else {
      showError("Niste unijeli korisničko ime!");
    }
  }
  else {
    if(loginPassword === "") {
      showError("Niste unijeli šifru!");
    }
  }
}