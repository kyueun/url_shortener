from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import re
from DBmanage import *
from base62 import *


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

invalid_str = 'invalid URL'
url_str = '{domain}/{subdomain}'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        value = request.form['result']

        # append protocol if not specified
        regex = re.compile(r'^(?:http|ftp)s?://')
        if re.match(regex, value) is None:
            value = 'https://' + value

        # remove www. to remove duplicated store
        value_list = value.split('www.')
        value = ''.join(value_list)

        try:
            # check if the url is valid
            headers = {'User-Agent': 'Chrome/66.0.3359.181'}
            req = urllib.request.Request(value, headers=headers)
            urllib.request.urlopen(req)

            insert_url(value)

            row = find_url(value)
            result = url_str.format(domain=app.config['SERVER_NAME'], subdomain=encode(row[0]))

        except:
            # in case of the url is invalid
            result = invalid_str

        return render_template('index.html', value=result)


@app.route('/<subdomain>')
def goto_url(subdomain):
    try:
        # check length of subdomain
        if len(subdomain)!=8:
            raise Exception

        # check if the url is exist in DB
        oldurl = find_oldurl(decode(subdomain))[1]
        result = redirect(oldurl)

    except:
        # in case of access to invalid url
        result = render_template('index.html', value=invalid_str)

    return result


if __name__ == '__main__':
    app.run(debug=False)