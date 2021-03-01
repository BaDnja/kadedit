const deleteForms = document.getElementsByClassName("form-delete");

for(let i = 0; i < forms.length; i++) {
    deleteForms[i].onsubmit = alertOnDelete;
}

function alertOnDelete() {
    const res = confirm("Da li ste sigurni da želite obrisati objekat?");

    if(res) {
        return true;
    }
    else return false;
}