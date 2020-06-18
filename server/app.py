from flask import Flask
from flask import request, send_from_directory
import json
import os
app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get_data():
    data = []
    with open("json/data.json", 'r') as f:
        data = json.load(f)
    return json.dumps(data)

@app.route('/upload', methods=['POST'])
def upload_file():
    img = request.files.get('file')
    outputfile = '/home/embed/'

    img_name = img.filename
    
    img.save(outputfile + img_name)
    os.system('./darknet detect cfg/yolov3.cfg yolov3.weights ' + outputfile + img_name)
    
    return 'Upload Successfully!'
@app.route('/download', methods=['GET','POST'])
def download_file():
    download_path = '/root/flask/app/darknet-master/'
    
    return send_from_directory(download_path, 'predictions.jpg', as_attachment=True)
@app.route('/', methods=['GET','POST'])
def index():
    return "hello"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
