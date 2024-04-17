// dragula([document.querySelector('#your-container')]);

dragula([document.getElementById('left1'), document.getElementById('middle1'), document.getElementById('right1')]);


function toggleToForm(elementId) {
    var currentElement = document.getElementById(elementId);
    var otherElementId = elementId === 'reorder-variables' ? 'reorder-paragraphs' : 'reorder-variables';
    var otherElement = document.getElementById(otherElementId);

    // Check if the other element is currently a form, revert if yes
    if (otherElement.tagName.toLowerCase() === 'form') {
        return;
    }

    // Toggle the current element to form if it is not already a form
    if (currentElement.tagName.toLowerCase() !== 'form') {
        var newElement = document.createElement('form');
        newElement.setAttribute('action', '#');
        newElement.setAttribute('method', 'post');

        // Example input and submit button
        // var input = document.createElement('input');
        // input.setAttribute('type', 'text');
        // input.setAttribute('name', 'exampleInput');
        // newElement.appendChild(input);

        var submitBtn = document.createElement('input');
        submitBtn.setAttribute('type', 'submit');
        submitBtn.setAttribute('value', 'Submit');
        newElement.appendChild(submitBtn);

        currentElement.parentNode.replaceChild(newElement, currentElement);
        newElement.setAttribute('id', elementId);  // preserve the ID for reversion
    } else {
        // If it is already a form, revert to div
        revertToDiv(elementId);
    }
}

function revertToDiv(elementId) {
    var formElement = document.getElementById(elementId);
    var newElement = document.createElement('div');
    newElement.setAttribute('id', elementId);

    formElement.parentNode.replaceChild(newElement, formElement);
}
