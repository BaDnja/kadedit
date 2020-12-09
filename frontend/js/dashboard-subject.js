const filterBox = document.getElementById('filter-box');
const btnAdvanced = document.getElementById('btn-advanced');

// Modals
const modalNewSubject = document.getElementById("modal-new-subject");
const modalAssistant = document.getElementById("modal-assistant");

// Buttons to open modals
const btnAddAssistant = document.getElementById("btn-add-new-assistant");
const btnAddAssistantModal = document.getElementById("btn-add-new-assistant1");
const btnAddNewSubject = document.getElementById("btn-add-new-subject");

// Buttons to close modals
const btnCloseModalAddAssistant = document.getElementById("btn-modal-assistant-close");
const btnCloseModalAddNewSubject = document.getElementById("btn-modal-add-close");

btnAddAssistant.addEventListener("click", switchModalSubject);
btnAddAssistantModal.addEventListener("click", switchModalSubject);
btnCloseModalAddAssistant.addEventListener("click", switchModalSubject);

btnAddNewSubject.addEventListener("click", switchModalProfessor);
btnCloseModalAddNewSubject.addEventListener("click", switchModalProfessor);




// Event to handle advanced filters 
btnAdvanced.addEventListener("click", showFilters);

function showFilters(e) {
    e.preventDefault();
    if(filterBox.style.display === "flex") {
      filterBox.style.display = "none";
    }
    else {
      filterBox.style.display = "flex";
    }
  }

  // Event to show / hide Subject modal
  function switchModalSubject() {
    if (modalAssistant.style.display === "flex") {
      modalAssistant.style.display = "none";
    }
    else modalAssistant.style.display = "flex";
  }

  function switchModalProfessor() {
    if (modalNewSubject.style.display === "flex") {
      modalNewSubject.style.display = "none";
    }
    else modalNewSubject.style.display = "flex";
  }
  // Event to show / hide professors modal