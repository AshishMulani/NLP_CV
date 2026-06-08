from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
app = Flask(__name__)

from nltk.corpus import stopwords
ps = PorterStemmer()
swords = stopwords.words('english')
def clean_text(sent):
    tokens1 = word_tokenize(sent)
    tokens2 = [token for token in tokens1 if token.isalpha()]
    tokens3 = [token.lower() for token in tokens2 if token.lower() not in swords]
    tokens4 = [ps.stem(token) for token in tokens3]
    return tokens4

classifier = joblib.load('model.bin')
tfidf = joblib.load('preprocess.bin')

@app.route('/')
def student():
    return render_template('spamdetector.html')

@app.route('/spamfinder', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message)[0]
        return render_template('spamoutput.html', data=data)

if __name__ == '__main__':
    app.run(debug = True)