from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    # Get JSON data
    data = request.json
    num_repeats = int(data['num_repeats'])
    d2 = int(data['d2'])
    d4 = int(data['d4'])
    d6 = int(data['d6'])
    d8 = int(data['d8'])
    d10 = int(data['d10'])
    d12 = int(data['d12'])
    d20 = int(data['d20'])
    d100 = int(data['d100'])

    # Process the data (e.g., perform dice rolls)
    # Return the result as JSON
    result = {
        'num_repeats': num_repeats,
        'd2': d2,
        'd4': d4,
        'd6': d6,
        'd8': d8,
        'd10': d10,
        'd12': d12,
        'd20': d20,
        'd100': d100
    }
    print(result)
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)
