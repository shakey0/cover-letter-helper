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
        input.value = ''; // Clear input after adding
    }
}

function addVarCode() {
    const input = document.getElementById('var-code-input');
    const varCode = input.value.trim();
    if (varCode) {
        const box = document.createElement('div');
        box.className = 'var-code'
        box.textContent = varCode

        
    }
}