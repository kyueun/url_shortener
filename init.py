from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import re
from DBmanage import find_url, find_oldurl, insert_url
from base62 import encode, decode

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

invalid_str = 'invalid URL'
url_str = '{server}/{index}'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        value = request.form['result']
        old_url = value

        regex = re.compile(r'^(?:http|ftp)s?://')
        if re.match(regex, value) is None:
            value = 'https://' + value

        value_list = value.split('www.')
        value = ''.join(value_list)

        try:
            res = urllib.request.urlopen(value)

            try:
                insert_url(value)

            except:
                pass

            row = find_url(value)
            result = url_str.format(server=app.config['SERVER_NAME'], index=encode(row[0]))

        except:
            result = invalid_str

        return render_template('index.html', value=result)


@app.route('/<url>')
def goto_url(url):
    try:
        oldurl = find_oldurl(decode(url))[1]
        result = redirect(oldurl)

    except:
        result = render_template('index.html', value=invalid_str)

    return result


if __name__ == '__main__':
    app.run(debug=False)