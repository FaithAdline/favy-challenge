from flask import Flask, jsonify

app = Flask(__name__)

# Challenge 1: Converting 12-hour time to 24-hour time
@app.route('/challenge1/<int:hour>/<int:minute>/<period>')
def challenge1(hour, minute, period):
    if period.lower() == 'am':
        if hour == 12:
            hour = 0
    elif period.lower() == 'pm':
        if hour != 12:
            hour += 12
    
    result = f"{hour:02d}{minute:02d}"
    
    return jsonify(result=result)

# Challenge 2: Two numbers are positive
@app.route('/challenge2/<int:a>/<int:b>/<int:c>')
def challenge2(a, b, c):
    positive_count = sum(1 for num in [a, b, c] if num > 0)
    result = positive_count == 2
    
    return jsonify(result=result)

# Challenge 3: Consonant value
@app.route('/challenge3/<string:word>')
def challenge3(word):
    consonant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    substrings = [consonant_values[word[i:j+1]] for i in range(len(word)) for j in range(i, len(word)) if word[i:j+1] not in 'aeiou']
    
    result = max(substrings, default=0)
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)



