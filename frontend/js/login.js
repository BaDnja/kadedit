const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');





loginForm.addEventListener("submit", validateLogin);


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
      // loginUsername = "" ili loginPassword = "" ne radi, jer je to samo kopija vrijednosti iz inputa. 
      // Da bi se input ocistio potrebno mu je direkt pristupiti
      showError("Niste unijeli ni korisničko ime ni šifru!");
      document.getElementById('login-username').value = "";
      document.getElementById('login-password').value = "";
      e.preventDefault();
    }
    else {
      showError("Niste unijeli korisničko ime!");
      document.getElementById('login-username').value = "";
      document.getElementById('login-password').value = "";
      e.preventDefault();
    }
  }
  else {
    if(loginPassword === "") {
      showError("Niste unijeli šifru!");
      document.getElementById('login-username').value = "";
      document.getElementById('login-password').value = "";
      e.preventDefault();
    }
  }
}

