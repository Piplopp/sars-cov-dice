function rollDice() {
    var formData = new FormData(document.getElementById('diceForm'));

    fetch('/roll_dice', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(html => {
            document.documentElement.innerHTML = html;
            // Handle response data (if any)
        })
        .catch(error => console.error('Error:', error));
}





function validateInput(inputField, errorContainer, inputFieldType) {
    var value = inputField.value.trim();

    // Let's remove existing error messages just in case
    if (errorContainer && errorContainer.classList.contains('invalid-input')) {
        errorContainer.innerHTML = '';
    } else {
        // Create the empty errorContainer if it does not exists
        errorContainer = document.createElement('div');
        errorContainer.className = 'invalid-input';
        inputField.parentNode.insertBefore(errorContainer, inputField.nextSibling);
    }

    // Now let's really validate stuff
    if (value !== '') {
        if (inputFieldType === 'diceInput') {
            if (!Number.isInteger(Number(value)) || Number(value) < 0) {
                // Change input field style
                inputField.style.borderColor = 'red';
                inputField.style.color = 'red';

                // Create error message
                var errorMessageElement = document.createElement('span');
                errorMessageElement.textContent = 'Must be an integer >= 0.';
                errorContainer.appendChild(errorMessageElement);
                return;
            }
        } else if (inputFieldType === 'repeatsInput') {
            if (!Number.isInteger(Number(value)) || Number(value) < 0) {
                // Change input field style
                inputField.style.borderColor = 'red';
                inputField.style.color = 'red';

                // Create error message
                var errorMessageElement = document.createElement('span');
                errorMessageElement.textContent = 'Must be an integer > 0';
                errorContainer.appendChild(errorMessageElement);
                return;
            }
        }
    }

    // Otherwise if input is valid, just reset the style
    inputField.style.borderColor = '';
    inputField.style.color = '';
}

function validateDiceInputs(){
    var diceInputs = document.querySelectorAll('.dice-inputs input');
    diceInputs.forEach(function(x) {
        validateInput(x, x.parentNode.parentNode.nextElementSibling, 'diceInput')
    });
}

function validateRepeatsInput(){
    var repeatsInput = document.getElementById('n_repeats');
    validateInput(repeatsInput, repeatsInput.parentNode.parentNode.nextElementSibling, 'repeatsInput')
}


function validateAllInputs() {
    validateDiceInputs();
    validateRepeatsInput();
}
