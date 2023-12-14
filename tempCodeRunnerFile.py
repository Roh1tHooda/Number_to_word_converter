from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

def number_to_words(number):
    # Define lists for words representing numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def recursive_convert(number):
        if number == 0:
            return ""
        elif number < 10:
            return ones[number]
        elif number < 20:
            return teens[number - 10]
        elif number < 100:
            return tens[number // 10] + " " + recursive_convert(number % 10)
        else:
            return ones[number // 100] + " hundred " + recursive_convert(number % 100)

    if number == 0:
        return "zero"
    
    words = ""
    for i in range(len(thousands)):
        if number % 1000 != 0:
            words = recursive_convert(number % 1000) + " " + thousands[i] + " " + words
        number //= 1000
adaaad
    return words.strip()

@app.route('/')
def home():
    return render_template('index.html')

def convert_number():
    try:
        data = request.get_json()
        if 'number' not in data:
            raise ValueError("Missing 'number' field in JSON input")
        
        number = int(data['number'])
        words = number_to_words(number)
        return jsonify({"success": True, "words": words})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
