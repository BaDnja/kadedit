const forms = document.getElementsByClassName("form-delete");


function alertOnDelete() {
    const res = confirm("Da li ste sigurni da želite obrisati objekat?");

    if(res) {
        return true;
    }
    else return false;
}

for(let i = 0; i < forms.length; i++) {
    forms[i].onsubmit = alertOnDelete;
}