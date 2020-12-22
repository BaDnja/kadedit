const filterBox = document.getElementById('filter-box');
//const btnAdvanced = document.getElementById('btn-advanced');

// Modals
const modalNewProfessor = document.getElementById("modal-new-professor");
const modalSubject = document.getElementById("modal-subject");

// Buttons to open modals
const btnAddSubject = document.getElementById("btn-add-new-subject");
const btnAddSubjectModal = document.getElementById("btn-add-new-subject1");
const btnAddNewProfessor = document.getElementById("btn-add-new-professor");

// Buttons to close modals
const btnCloseModalAddSubject = document.getElementById("btn-modal-subject-close");
const btnCloseModalAddNewProfessor = document.getElementById("btn-modal-add-close");

btnAddSubject.addEventListener("click", switchModalSubject);
btnAddSubjectModal.addEventListener("click", switchModalSubject);
btnCloseModalAddSubject.addEventListener("click", switchModalSubject);

btnAddNewProfessor.addEventListener("click", switchModalProfessor);
btnCloseModalAddNewProfessor.addEventListener("click", switchModalProfessor);




// Event to handle advanced filters
// btnAdvanced.addEventListener("click", showFilters);
//
// function showFilters(e) {
//     e.preventDefault();
//     if(filterBox.style.display === "flex") {
//       filterBox.style.display = "none";
//     }
//     else {
//       filterBox.style.display = "flex";
//     }
//   }

  // Event to show / hide Subject modal
  function switchModalSubject() {
    if (modalSubject.style.display === "flex") {
      modalSubject.style.display = "none";
    }
    else modalSubject.style.display = "flex";
  }

  function switchModalProfessor() {
    if (modalNewProfessor.style.display === "flex") {
      modalNewProfessor.style.display = "none";
    }
    else modalNewProfessor.style.display = "flex";
  }
  // Event to show / hide professors modal