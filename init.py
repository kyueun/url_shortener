from flask import Flask, render_template, request, redirect
from DBmanage import find_url, find_oldurl, insert_url
from base62 import encode, decode

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method=='POST':
        value = request.form['result']

        row = find_url(value)
        if row==None:
            insert_url(value)
            row = find_url(value)

        result = encode(row[0])
        result = 'localhost:5000/'+result

        return result

@app.route('/<url>')
def goto_url(url):
    oldurl = find_oldurl(decode(url))
    return redirect(oldurl)

if __name__=='__main__':
    app.run(debug=True)