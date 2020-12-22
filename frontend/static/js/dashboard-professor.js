const modalSubject = document.getElementById("modal-subject");


const btnOpenModalSubject = document.getElementById("btn-modal-subject-open");
const btnCloseModalSubject = document.getElementById("btn-modal-subject-close");



btnOpenModalSubject.addEventListener("click", switchModal);
btnCloseModalSubject.addEventListener("click",  switchModal);

function switchModal() {
    if(modalSubject.style.display === "none") {
        modalSubject.style.display = "flex";
    } else {
        modalSubject.style.display = "none";
    }
}


