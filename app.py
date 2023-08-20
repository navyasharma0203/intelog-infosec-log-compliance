from flask import Flask, render_template, request, redirect, url_for
import os
import joblib
from transformers import BertForSequenceClassification
from werkzeug.utils import secure_filename
from model import process_compliance_logs  # Import your compliance logs processing function

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv', 'txt', 'log'}  # Update with allowed file extensions

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_files():
#     try:
#         # Get uploaded files from the request
#         files = request.files.getlist('file-upload-field')

#         # Check if files are uploaded
#         if len(files) == 0:
#             return redirect(request.url)

#         # Process uploaded files using your model's function
#         results = process_compliance_logs(files)  # Replace with your processing logic

#         return render_template('user.html', results=results)  # Pass the results to the template

#     except Exception as e:
#         return render_template('user.html', error=str(e))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Use your trained model to process the file and generate results
        result = your_trained_model.process(file_path)
           
        return render_template('user.html', result=result)  # Pass the results to the template

if __name__ == '__main__':
    app.run(debug=True)

