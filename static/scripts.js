function rollDice() {
    var formData = new FormData(document.getElementById('diceForm'));
    formData.append('num_dice', 8); // You need to add num_dice manually or dynamically calculate it based on the user's input
    fetch('/roll_dice', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle response data (if any)
        })
        .catch(error => console.error('Error:', error));
}
