function addVar() {
    const input = document.getElementById('var-input');
    const variable = input.value.trim();
    if (variable) {
        const box = document.createElement('div');
        box.className = 'var-box';
        const boxText = document.createElement('p');
        boxText.textContent = variable;
        box.appendChild(boxText);
        const inputHidden = document.createElement('input');
        inputHidden.type = 'hidden';
        inputHidden.name = 'variables[]';
        inputHidden.value = variable;
        box.appendChild(inputHidden);

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
        const varCodeActInput = document.getElementById('var-code-act-input');
        varCodeActInput.value = varCode
        varCodeAct.style.display = 'block'
        document.getElementById('edit-var-code-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('var-code-btn').style.display = 'none';
        
        const varCodeMesLc = document.getElementById('var-code-mes-lc')
        const varCodeMesMin = document.getElementById('var-code-mes-min')
        const varCodeMes = document.getElementById('var-code-mes')
        varCodeMesLc.style.color = '#1f1f1f'
        varCodeMesMin.style.color = '#1f1f1f'
        varCodeMes.style.display = 'none'

    } else if (varCode && varCode.length < 4) {
        const varCodeMesMin = document.getElementById('var-code-mes-min')
        varCodeMesMin.style.color = 'red'
    }
}

function editVarCode() {
    const input = document.getElementById('var-code-input');
    input.style.display = 'block';
    const varCodeAct = document.getElementById('var-code-act')
    input.value = varCodeAct.textContent
    const varCodeMes = document.getElementById('var-code-mes')
    varCodeMes.style.display = 'block'
    document.getElementById('var-code-btn').style.display = 'block';
    varCodeAct.style.display = 'none';
    document.getElementById('edit-var-code-btn').style.display = 'none';
}

const varCodeController = document.getElementById('var-code-input')
if (varCodeController) {
    varCodeController.addEventListener('input', function() {
        if (/[^a-z*]/.test(this.value)) {
            const varCodeMesLc = document.getElementById('var-code-mes-lc')
            varCodeMesLc.style.color = 'red'
        }
        let cleanInput = this.value = this.value.toLowerCase().replace(/[^a-z]/g, '');
        if (!cleanInput.startsWith('**')) {
            cleanInput = '**' + cleanInput;
        }
        this.value = cleanInput;
    });
}

// const saveListBtn = document.getElementById('save-list-btn');
// saveListBtn.addEventListener('submit', function(event) {
//     const varCodeActInput = document.getElementById('var-code-act')
//     const varContainer = document.getElementById('var-container')
//     if (varCodeActInput.value.length < 4 && varContainer.children.length < 1) {
//         event.preventDefault();
//         alert('Please add at least one variable and a variable code');
//     }
// });