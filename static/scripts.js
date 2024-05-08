function rollDice() {
    var formData = new FormData(document.getElementById('diceForm'));

    fetch('/roll_dice', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(Object.fromEntries(formData))
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle response data (if any)
        })
        .catch(error => console.error('Error:', error));
}
