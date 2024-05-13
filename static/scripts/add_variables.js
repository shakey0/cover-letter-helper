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
        deleteBtn.type = 'button';
        deleteBtn.onclick = function () {
            box.remove();
        };

        box.appendChild(deleteBtn);
        document.getElementById('var-container').appendChild(box);
        input.value = '';
    }
}

document.getElementById('var-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        addVar();
    }
});

function addListName() {
    const input = document.getElementById('list-name-input');
    const listName = input.value.trim();
    if (listName) {
        const listNameAct = document.getElementById('list-name-act');
        listNameAct.textContent = listName;
        listNameAct.style.display = 'block';
        document.getElementById('list-name-act-input').value = listName;
        document.getElementById('edit-list-name-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('list-name-btn').style.display = 'none';
    }
}

function editListName() {
    const input = document.getElementById('list-name-input');
    input.style.display = 'block';
    const listNameAct = document.getElementById('list-name-act');
    input.value = listNameAct.textContent;
    listNameAct.style.display = 'none';

    document.getElementById('list-name-btn').style.display = 'block';
    document.getElementById('edit-list-name-btn').style.display = 'none';
}

function addVarCode() {
    const input = document.getElementById('var-code-input');
    const varCode = input.value.trim();
    if (varCode && varCode.length >= 4) {
        const varCodeAct = document.getElementById('var-code-act');
        varCodeAct.textContent = varCode;
        varCodeAct.style.display = 'block';
        document.getElementById('var-code-act-input').value = varCode;
        document.getElementById('edit-var-code-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('var-code-btn').style.display = 'none';
        
        document.getElementById('var-code-mes-lc').style.color = '#1f1f1f';
        document.getElementById('var-code-mes-min').style.color = '#1f1f1f';
        document.getElementById('var-code-mes').style.display = 'none';

    } else if (varCode && varCode.length < 4) {
        document.getElementById('var-code-mes-min').style.color = 'red';
    }
}

function editVarCode() {
    const input = document.getElementById('var-code-input');
    input.style.display = 'block';
    const varCodeAct = document.getElementById('var-code-act');
    input.value = varCodeAct.textContent;
    varCodeAct.style.display = 'none';

    document.getElementById('var-code-mes').style.display = 'block';
    document.getElementById('var-code-btn').style.display = 'block';
    document.getElementById('edit-var-code-btn').style.display = 'none';
}

const varCodeController = document.getElementById('var-code-input')
if (varCodeController) {
    varCodeController.addEventListener('input', function() {
        if (/[^a-z*]/.test(this.value)) {
            document.getElementById('var-code-mes-lc').style.color = 'red';
        }
        let cleanInput = this.value = this.value.toLowerCase().replace(/[^a-z]/g, '');
        if (!cleanInput.startsWith('**')) {
            cleanInput = '**' + cleanInput;
        }
        this.value = cleanInput;
    });
}

const saveListBtn = document.getElementById('save-list-btn');
const saveListForm = saveListBtn.closest('form');
saveListForm.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
    }
});

saveListForm.addEventListener('submit', function(event) {
    const listNameActInput = document.getElementById('list-name-act-input');
    const varCodeActInput = document.getElementById('var-code-act-input');
    const varContainer = document.getElementById('var-container');
    const varCodeAct = document.getElementById('var-code-act');
    const listNameAct = document.getElementById('list-name-act');

    if (listNameActInput.value.length < 1 || varCodeActInput.value.length < 4 || varContainer.children.length < 1 || listNameAct.style.display === 'none' || varCodeAct.style.display === 'none') {
        event.preventDefault();
    }
});

document.body.addEventListener('keydown', function(event) {
    if (event.target.id === 'list-name-input' || event.target.id === 'list-name-btn') {
        if (event.key === 'Enter') {
            addListName();
        }
    }
    if (event.target.id === 'var-code-input' || event.target.id === 'var-code-btn') {
        if (event.key === 'Enter') {
            addVarCode();
        }
    }
    if (event.target.id === 'var-input' || event.target.id === 'var-btn') {
        if (event.key === 'Enter') {
            addVar();
        }
    }
});