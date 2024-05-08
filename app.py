from flask import Flask, request, jsonify, render_template
from forms.dice_form import DiceForm

app = Flask(__name__)

@app.route('/')
def index():
    dice_form = DiceForm()
    return render_template('index.html', dice_form=dice_form)

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    # Get JSON data
    data = DiceForm(request.form)
    data.validate()
    
    
    return render_template('index.html', dice_form=data)



if __name__ == "__main__":
    app.run(debug=True)
