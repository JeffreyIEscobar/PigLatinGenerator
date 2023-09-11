from flask import Flask, render_template, request

app = Flask(__name__)

def pig_latin(text):
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word[0] in "aeiouAEIOU":
            pig_latin_word = word + "way"
        else:
            pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)

    return ' '.join(pig_latin_words)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        pig_latin_text = pig_latin(input_text)
        return render_template('index.html', input_text=input_text, pig_latin_text=pig_latin_text)
    return render_template('index.html', input_text='', pig_latin_text='')

if __name__ == '__main__':
    app.run(debug=True)
