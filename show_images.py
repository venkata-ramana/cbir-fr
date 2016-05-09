#!/bin/python

import os
from flask import Flask, Response, request, abort, render_template_string, send_from_directory
import Image
import StringIO

app = Flask(__name__)

WIDTH = 1000
HEIGHT = 800

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <style>
body {
    margin: 0;
    background-color: #fff;
}
.imglink{
	font-size:12px;
    font-family:
    font-family: serif;
	color:#1D1D1D;
	text-decoration: none;
}
.image {
    background-color:#fff;
	text-align:center;
    margin: 1px 3px 5px 1px;
    box-shadow: 0 0 10px gray;
    display: inline-block;
    width:120px;
    height:130px;
}
img {
    display: inline-block;
    width:120px;
    height:100px;
}

    </style>

   
</head>
<body>
    <center>
    {% for image in images %}
    <div class="image">
        <a class='imglink' href="{{ image.src }}">
    	<img src="{{ image.src }}"/>
        {{image.src}}</a>
    </div>
    {% endfor %}
    </center>
</body>
'''

@app.route('/<path:filename>')
def image(filename):
    try:
        w = int(request.args['w'])
        h = int(request.args['h'])
    except (KeyError, ValueError):
        return send_from_directory('.', filename)

    try:
        im = Image.open(filename)
        im.thumbnail((w, h), Image.ANTIALIAS)
        io = StringIO.StringIO()
        im.save(io, format='JPEG')
        return Response(io.getvalue(), mimetype='image/jpeg')

    except IOError:
        abort(404)

    return send_from_directory('.', filename)

@app.route('/')
def index():
    images = []
    i=0
    for root, dirs, files in os.walk('dataset2'):
        for filename in [os.path.join(root, name) for name in files]:
            if not filename.endswith('.png'):
                continue
            if (i>50):
                break
            im = Image.open(filename)
            images.append({
                'src': filename
            })
            i+=1

    return render_template_string(TEMPLATE, **{
        'images': images
    })

if __name__ == '__main__':
    app.run(debug=True, host='::')