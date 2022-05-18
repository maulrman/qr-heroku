import mimetypes
import os
import qrcode
from io import BytesIO
from flask import Flask, redirect, render_template, request, send_file, url_for

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if request.form['link-data']:
            return redirect(url_for('qrify', data=request.form['link-data']))
        else:
            pass
            #create error
    return render_template('index.html')

@app.route('/qr/<data>')
def serve_qr(data):
    img = qrcode.make(data)
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/qr')
def gen_qr(data):
    img = qrcode.make(request.args.get('data'))
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/qrify/<data>')
def qrify(data):
    context = {
        'data': data,
    }
    return render_template('qrify.html', context=context)
