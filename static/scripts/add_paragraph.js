function addParagraphName() {
    const input = document.getElementById('paragraph-name-input');
    const paragraphName = input.value.trim();
    if (paragraphName) {
        const paragraphNameAct = document.getElementById('paragraph-name-act');
        paragraphNameAct.textContent = paragraphName;
        paragraphNameAct.style.display = 'block';
        document.getElementById('paragraph-name-act-input').value = paragraphName;
        document.getElementById('edit-paragraph-name-btn').style.display = 'block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('paragraph-name-btn').style.display = 'none';
    }
}

document.getElementById('paragraph-name-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        addParagraphName();
    }
});

function editParagraphName() {
    const input = document.getElementById('paragraph-name-input');
    input.style.display = 'block';
    const paragraphNameAct = document.getElementById('paragraph-name-act');
    input.value = paragraphNameAct.textContent;
    paragraphNameAct.style.display = 'none';

    document.getElementById('paragraph-name-btn').style.display = 'block';
    document.getElementById('edit-paragraph-name-btn').style.display = 'none';
}

function addParagraphText() {
    const input = document.getElementById('paragraph-text-input');
    const paragraphText = input.value.trim();
    if (paragraphText) {
        const paragraphTextAct = document.getElementById('paragraph-text-act');
        paragraphTextAct.textContent = paragraphText;
        paragraphTextAct.style.display = 'block';
        document.getElementById('paragraph-text-act-input').value = paragraphText;
        document.getElementById('edit-paragraph-text-btn').style.display = 'inline-block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('paragraph-text-btn').style.display = 'none';
    }
}

document.getElementById('paragraph-text-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        addParagraphText();
    }
});

function editParagraphText() {
    const input = document.getElementById('paragraph-text-input');
    input.style.display = 'block';
    const paragraphTextAct = document.getElementById('paragraph-text-act');
    input.value = paragraphTextAct.textContent;
    paragraphTextAct.style.display = 'none';

    document.getElementById('paragraph-text-btn').style.display = 'block';
    document.getElementById('edit-paragraph-text-btn').style.display = 'none';
}

const saveParagraphBtn = document.getElementById('save-paragraph-btn');
const saveParagraphForm = saveParagraphBtn.closest('form');
saveParagraphForm.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
    }
});

saveParagraphForm.addEventListener('submit', function(event) {
    const paragraphNameActInput = document.getElementById('input-name-act-input');
    const paragraphTextActInput = document.getElementById('input-code-act-input');

    if (paragraphNameActInput.value.length < 1 || paragraphTextActInput.value.length < 1) {
        event.preventDefault();
    }
});
