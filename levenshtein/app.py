# app.py
from flask import Flask, request, render_template
import pandas as pd
import nltk

nltk.download('words')
from nltk.corpus import words

app = Flask(__name__)

word_list = words.words()


def levenshtein_distance(s1, s2):
    df = pd.DataFrame(index=range(len(s1) + 1), columns=range(len(s2) + 1))

    for i in range(len(s1) + 1):
        df.at[i, 0] = i
    for j in range(len(s2) + 1):
        df.at[0, j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            df.at[i, j] = min(
                df.at[i - 1, j] + 1,
                df.at[i, j - 1] + 1,
                df.at[i - 1, j - 1] + cost
            )

    return df.at[len(s1), len(s2)]


def find_closest_word(input_word, word_list):
    closest_word = None
    min_distance = float('inf')

    for word in word_list:
        distance = levenshtein_distance(input_word, word)
        if distance < min_distance:
            min_distance = distance
            closest_word = word

    return closest_word


@app.route('/', methods=['GET', 'POST'])
def index():
    closest_word = None
    input_word = ''

    if request.method == 'POST':
        input_word = request.form['word']
        closest_word = find_closest_word(input_word, word_list)

    return render_template('index.html', closest_word=closest_word, input_word=input_word)


if __name__ == '__main__':
    app.run(debug=True)
