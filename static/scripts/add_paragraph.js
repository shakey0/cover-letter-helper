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
        document.getElementById('paragraph-name-error').textContent = '';
    }
}

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
        paragraphTextAct.innerHTML = emphasiseVars(paragraphText);
        paragraphTextAct.style.display = 'block';
        document.getElementById('paragraph-text-act-input').value = paragraphText;
        document.getElementById('edit-paragraph-text-btn').style.display = 'inline-block';

        input.value = '';
        input.style.display = 'none';
        document.getElementById('paragraph-text-btn').style.display = 'none';
        document.getElementById('paragraph-text-error').textContent = '';
    }
}

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
    const paragraphNameActInput = document.getElementById('paragraph-name-act-input');
    const paragraphTextActInput = document.getElementById('paragraph-text-act-input');
    const paragraphNameAct = document.getElementById('paragraph-name-act');
    const paragraphTextAct = document.getElementById('paragraph-text-act');

    if (paragraphNameActInput.value.length < 1 || paragraphTextActInput.value.length < 1 || paragraphNameAct.style.display === 'none' || paragraphTextAct.style.display === 'none') {
        event.preventDefault();
    } else {
        event.preventDefault();

        var formData = new FormData(saveParagraphForm);
        var formAction = saveParagraphForm.getAttribute('action');

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
                    document.getElementById('paragraph-name-error').textContent = data.error;
                } else if (data.error.includes('has not been created')) {
                    document.getElementById('paragraph-text-error').textContent = data.error;
                }
            }
        });
    }
});

document.body.addEventListener('keydown', function(event) {
    if (event.target.id === 'paragraph-name-input' || event.target.id === 'paragraph-name-btn') {
        if (event.key === 'Enter') {
            addParagraphName();
        }
    }
    if (event.target.id === 'paragraph-text-input' || event.target.id === 'paragraph-text-btn') {
        if (event.key === 'Enter') {
            addParagraphText();
        }
    }
});

function emphasiseVars(text) {
    var regex = /(\*\*|##)\w+/g;
    var result = text.replace(regex, function(match) {
        return '<strong class="emphasise">' + match + '</strong>';
    });
    return result;
}