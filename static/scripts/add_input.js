function addInputName() {
    const input = document.getElementById('input-name-input');
    const inputName = input.value.trim();
    if (inputName) {
        const inputNameAct = document.getElementById('input-name-act');
        inputNameAct.textContent = inputName;
        inputNameAct.style.display = 'block';
        document.getElementById('input-name-act-input').value = inputName;
        document.getElementById('edit-input-name-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('input-name-btn').style.display = 'none';
        document.getElementById('input-name-error').textContent = '';

        code_input = document.getElementById('input-code-input');
        if (code_input.style.display !== 'none') {
            code_input.focus();
            const value = code_input.value;
            code_input.value = '';
            code_input.value = value;
        }
    }
}

function editInputName() {
    const input = document.getElementById('input-name-input');
    input.style.display = 'block';
    input.focus();
    const inputNameAct = document.getElementById('input-name-act');
    input.value = inputNameAct.textContent;
    inputNameAct.style.display = 'none';

    document.getElementById('input-name-btn').style.display = 'block';
    document.getElementById('edit-input-name-btn').style.display = 'none';
}

function addInputCode() {
    const input = document.getElementById('input-code-input');
    const inputCode = input.value.trim();
    if (inputCode && inputCode.length >= 4) {
        const inputCodeAct = document.getElementById('input-code-act');
        inputCodeAct.textContent = inputCode;
        inputCodeAct.style.display = 'block';
        document.getElementById('input-code-act-input').value = inputCode;
        document.getElementById('edit-input-code-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('input-code-btn').style.display = 'none';
        document.getElementById('input-code-error').textContent = '';
        
        document.getElementById('input-code-mes-lc').style.color = '#1f1f1f';
        document.getElementById('input-code-mes-min').style.color = '#1f1f1f';
        document.getElementById('input-code-mes').style.display = 'none';

        name_input = document.getElementById('input-name-input');
        if (name_input.style.display !== 'none') {
            name_input.focus();
            const value = name_input.value;
            name_input.value = '';
            name_input.value = value;
        }

    } else if (inputCode && inputCode.length < 4) {
        document.getElementById('input-code-mes-min').style.color = 'red';
    }
}

function editInputCode() {
    const input = document.getElementById('input-code-input');
    input.style.display = 'block';
    input.focus();
    const inputCodeAct = document.getElementById('input-code-act');
    input.value = inputCodeAct.textContent;
    inputCodeAct.style.display = 'none';

    document.getElementById('input-code-mes').style.display = 'block';
    document.getElementById('input-code-btn').style.display = 'block';
    document.getElementById('edit-input-code-btn').style.display = 'none';
}

const inputCodeController = document.getElementById('input-code-input')
if (inputCodeController) {
    inputCodeController.addEventListener('input', function() {
        if (/[^a-z#]/.test(this.value)) {
            document.getElementById('input-code-mes-lc').style.color = 'red';
        }
        let cleanInput = this.value = this.value.toLowerCase().replace(/[^a-z]/g, '');
        if (!cleanInput.startsWith('##')) {
            cleanInput = '##' + cleanInput;
        }
        this.value = cleanInput;
    });
}

const saveInputBtn = document.getElementById('save-input-btn');
const saveInputForm = saveInputBtn.closest('form');
saveInputForm.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
    }
});

saveInputForm.addEventListener('submit', function(event) {
    const inputNameActInput = document.getElementById('input-name-act-input');
    const inputCodeActInput = document.getElementById('input-code-act-input');
    const inputNameAct = document.getElementById('input-name-act');
    const inputCodeAct = document.getElementById('input-code-act');

    if (inputNameActInput.value.length < 1 || inputCodeActInput.value.length < 4 || inputNameAct.style.display === 'none' || inputCodeAct.style.display === 'none') {
        event.preventDefault();
    } else {
        event.preventDefault();

        var formData = new FormData(saveInputForm);
        var formAction = saveInputForm.getAttribute('action');
        
        fetch(formAction, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect;
            } else {
                if (data.error.includes('Name')) {
                    document.getElementById('input-name-error').textContent = data.error;
                } else if (data.error.includes('Code')) {
                    document.getElementById('input-code-error').textContent = data.error;
                }                
            }
        });
    }
});

document.body.addEventListener('keydown', function(event) {
    if (event.target.id === 'input-name-input' || event.target.id === 'input-name-btn') {
        if (event.key === 'Enter') {
            addInputName();
        }
    }
    if (event.target.id === 'input-code-input' || event.target.id === 'input-code-btn') {
        if (event.key === 'Enter') {
            addInputCode();
        }
    }
});

const deleteInputBtn = document.getElementById('delete-input-btn');
const deleteInputBox = document.getElementById('delete-input-box');
let deleteInputBoxOpen = false;

function closeDeleteInput() {
    deleteInputBoxOpen = false;
    deleteInputBox.style.display = 'none';
}

function deleteInput() {
    if (deleteInputBoxOpen) {
        closeDeleteInput();
        return;
    }
    deleteInputBoxOpen = true;
    deleteInputBox.style.display = 'block';
}

function hideModal(event) {
    if (!deleteInputBox.contains(event.target) && !deleteInputBtn.contains(event.target)) {
        closeDeleteInput();
    }
}

function confirmDeleteInput() {
    const deleteInputForm = document.getElementById('delete-input-form');

    var formData = new FormData(deleteInputForm);
    var formAction = deleteInputForm.getAttribute('action');

    fetch(formAction, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect;
        }
    });
}

if (deleteInputBtn) {
    window.addEventListener('click', hideModal);
}