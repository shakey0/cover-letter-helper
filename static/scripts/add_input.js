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
    }
}

document.getElementById('input-name-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        addInputName();
    }
});

function editInputName() {
    const input = document.getElementById('input-name-input');
    input.style.display = 'block';
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
        
        document.getElementById('input-code-mes-lc').style.color = '#1f1f1f';
        document.getElementById('input-code-mes-min').style.color = '#1f1f1f';
        document.getElementById('input-code-mes').style.display = 'none';

    } else if (inputCode && inputCode.length < 4) {
        document.getElementById('input-code-mes-min').style.color = 'red';
    }
}

document.getElementById('input-code-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        addInputCode();
    }
});

function editInputCode() {
    const input = document.getElementById('input-code-input');
    input.style.display = 'block';
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

    if (inputNameActInput.value.length < 1 || inputCodeActInput.value.length < 4) {
        event.preventDefault();
    }
});
