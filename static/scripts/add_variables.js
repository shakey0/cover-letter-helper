function addVar() {
    const input = document.getElementById('var-input');
    const variable = input.value.trim();
    if (variable) {
        const box = document.createElement('div');
        box.className = 'var-box';
        box.textContent = variable;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'x';
        deleteBtn.className = 'delete-btn';
        deleteBtn.onclick = function () {
            box.remove();
        };

        box.appendChild(deleteBtn);
        document.getElementById('var-container').appendChild(box);
        input.value = '';
    }
}

function addVarCode() {
    const input = document.getElementById('var-code-input');
    const varCode = input.value.trim();
    if (varCode && varCode.length >= 4) {
        const varCodeAct = document.getElementById('var-code-act');
        varCodeAct.textContent = varCode
        varCodeAct.style.display = 'block'
        document.getElementById('edit-var-code-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('var-code-btn').style.display = 'none';
    }
}

function editVarCode() {
    const input = document.getElementById('var-code-input');
    input.style.display = 'block';
    const varCodeAct = document.getElementById('var-code-act')
    input.value = varCodeAct.textContent
    document.getElementById('var-code-btn').style.display = 'block';
    varCodeAct.style.display = 'none';
    document.getElementById('edit-var-code-btn').style.display = 'none';
}

const varCodeController = document.getElementById('var-code-input')
if (varCodeController) {
    varCodeController.addEventListener('input', function() {
        cleanInput = this.value = this.value.toLowerCase().replace(/[^a-z]/g, '');
        if (!cleanInput.startsWith('**')) {
            cleanInput = '**' + cleanInput;
        }
        this.value = cleanInput;
    });
}
