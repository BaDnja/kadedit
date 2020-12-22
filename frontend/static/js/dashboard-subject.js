const modalAssistant = document.getElementById('modal-assistant');

const btnOpenModalAssistant = document.getElementById(
  'btn-modal-assistant-open'
);
const btnCloseModalAssistant = document.getElementById(
  'btn-modal-assistant-close'
);

btnOpenModalAssistant.addEventListener('click', switchModal);
btnCloseModalAssistant.addEventListener('click', switchModal);

function switchModal() {
  if (modalAssistant.style.display === 'none') {
    modalAssistant.style.display = 'flex';
  } else {
    modalAssistant.style.display = 'none';
  }
}
