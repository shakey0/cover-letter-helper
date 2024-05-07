dragula([document.getElementById('left1'), document.getElementById('middle1'), document.getElementById('right1')]);

dragula([document.getElementById('reorder-inputs')]);

dragula([document.getElementById('reorder-variables')]);

dragula([document.getElementById('reorder-paragraphs')]);

dragula([document.getElementById('var-container')]);


document.addEventListener('DOMContentLoaded', function() {
    function setupEmphasiseVarsListeners() {
        const elements = Array.from(document.getElementsByClassName('emphasise-vars'));
        elements.forEach(function(element) {
            element.innerHTML = emphasiseVars(element.textContent);
        });
    }

    setupEmphasiseVarsListeners();

    const button = document.getElementById('paragraph-text-btn');
    button.addEventListener('click', function() {
        setupEmphasiseVarsListeners();
    });
    const input = document.getElementById('paragraph-text-input');
    input.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            setupEmphasiseVarsListeners();
        }
    });
});

function emphasiseVars(text) {
    var regex = /(\*\*|##)\w+/g;
    var result = text.replace(regex, function(match) {
        return '<strong class="emphasise">' + match + '</strong>';
    });
    return result;
}
