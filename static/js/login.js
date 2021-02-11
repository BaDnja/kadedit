const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');
const usernameInput = document.getElementById('login-username');
const passwordInput = document.getElementById('login-password');

loginForm.addEventListener('submit', validateLogin);
// usernameInput.addEventListener('invalid', (e) => {
//   checkValidity(e, 'Niste unijeli korisničko ime!');
// });
// passwordInput.addEventListener('invalid', (e) => {
//   checkValidity(e, 'Niste unijeli šifru!');
// });

// function checkValidity(e, msg) {
//   console.log(e.target.value)
//   if(e.target.value === ""){
//     e.target.setCustomValidity(msg);
//   }
// }

function showError(text) {
  loginError.style.visibility = 'visible';
  loginError.innerHTML = text;
  setTimeout(() => {
    loginError.style.visibility = 'hidden';
  }, 2000);
}
function validateLogin(e) {
  const loginUsername = document.getElementById('login-username').value;
  const loginPassword = document.getElementById('login-password').value;
  if (loginUsername === '') {
    if (loginPassword === '') {
      showError('Niste unijeli ni korisničko ime ni šifru!');
      document.getElementById('login-username').value = '';
      document.getElementById('login-password').value = '';
      e.preventDefault();
      return false;
    } else {
      showError('Niste unijeli korisničko ime!');
      document.getElementById('login-username').value = '';
      document.getElementById('login-password').value = '';
      e.preventDefault();
    }
  } else {
    if (loginPassword === '') {
      showError('Niste unijeli šifru!');
      document.getElementById('login-username').value = '';
      document.getElementById('login-password').value = '';
      e.preventDefault();
    }
  }
}
