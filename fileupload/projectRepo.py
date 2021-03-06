from flask import Flask
from flask.globals import request
from flask.helpers import url_for, send_file
from flask.templating import render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt','zip','c'])

app.config['UPLOAD_FOLDER'] = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),"uploads")
app.debug = True


@app.route('/')
def index():
    return render_template("content.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "done"
        else:
            return ""



if __name__ == '__main__':
    print(app.url_map)
    app.run(threaded=True)

