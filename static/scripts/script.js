dragula([document.getElementById('left1'), document.getElementById('middle1'), document.getElementById('right1')]);

dragula([document.getElementById('reorder-inputs')])
    .on('drop', function (el, target, source, sibling) {
        let order = Array.from(target.children).map(function(item, index) {
        return item.getAttribute('data-id');
        });

        fetch('/update-order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ order: order, type: 'inputs' })
        })
        .then(response => response.json())
        .then(data => {
        console.log('Input order updated', data);
        })
        .catch(error => console.error('Error updating order:', error));
    });


dragula([document.getElementById('reorder-variables')])
    .on('drop', function (el, target, source, sibling) {
        let order = Array.from(target.children).map(function(item, index) {
        return item.getAttribute('data-id');
        });

        fetch('/update-order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ order: order, type: 'variables_sets' })
        })
        .then(response => response.json())
        .then(data => {
        console.log('Variable order updated', data);
        })
        .catch(error => console.error('Error updating order:', error));
    });

dragula([document.getElementById('reorder-paragraphs')])
    .on('drop', function (el, target, source, sibling) {
        let order = Array.from(target.children).map(function(item, index) {
        return item.getAttribute('data-id');
        });

        fetch('/update-order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ order: order, type: 'paragraphs' })
        })
        .then(response => response.json())
        .then(data => {
        console.log('Paragraph order updated', data);
        })
        .catch(error => console.error('Error updating order:', error));
    });

dragula([document.getElementById('var-container')]);


document.addEventListener('DOMContentLoaded', function() {
    function setupEmphasiseVarsListeners() {
        const elements = Array.from(document.getElementsByClassName('emphasise-vars'));
        elements.forEach(function(element) {
            element.innerHTML = emphasiseVars(element.textContent);
        });
    }

    setupEmphasiseVarsListeners();
});

function emphasiseVars(text) {
    var regex = /(\*\*|##)\w+/g;
    var result = text.replace(regex, function(match) {
        return '<strong class="emphasise">' + match + '</strong>';
    });
    return result;
}