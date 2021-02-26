const deleteForms = document.getElementsByClassName("form-delete");

const forms = document.getElementsByTagName('form');

for(let i = 0; i < deleteForms.length; i++) {
    deleteForms[i].onsubmit = alertOnDelete;
}

function alertOnDelete() {
    const res = confirm("Da li ste sigurni da želite obrisati objekat?");

    if(res) {
        return true;
    }
    else return false;
}

for(let i = 0; i < forms.length; i++) {
    const inputs = forms[i].getElementsByTagName("input");
    let addEvent = false;
    for(let z = 0; z < inputs.length; z++) {
        if(inputs[z].type === "text" && inputs[z].required === true)
            addEvent = true;
        } 
        console.log(addEvent);
    if(inputs !== null && addEvent === true) forms[i].onsubmit = alertOnEmptyField.bind(this, inputs);      
}

function alertOnEmptyField(inputs) {

        for(let j = 0; j < inputs.length; j++) {
            if(inputs[j].value === " ") {
            alert("Obavezna polja su prazna!");
            return false;
            }
        }
}