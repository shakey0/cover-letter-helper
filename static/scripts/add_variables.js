function addWord() {
    const input = document.getElementById('wordInput');
    const word = input.value.trim();
    if (word) {
        const box = document.createElement('div');
        box.className = 'word-box';
        box.textContent = word;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'x';
        deleteBtn.className = 'delete-btn';
        deleteBtn.onclick = function () {
            box.remove();
        };

        box.appendChild(deleteBtn);
        document.getElementById('wordContainer').appendChild(box);
        input.value = ''; // Clear input after adding
    }
}
