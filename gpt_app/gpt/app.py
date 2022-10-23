from flask import Flask, request, g, render_template, redirect, session, flash
from gpt3 import setOpenai
from gptRun import GPTRunning
app = Flask(__name__, template_folder='templates')

GPTRunningInstance = GPTRunning("")
# configurate the folder for csv files that uploaded by users
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['GET'])
def index():
    return {'name':'asda'}
    
@app.route('/', methods = ['POST'])
def mainPage():
    if request.method == 'POST':
        request_data = request.data
        uploadFile = request_data['content'][0]
        description = request_data['content'][0]

        fileName = file.filename
        
        if GPTRunningInstance.getFile() == "" or GPTRunningInstance.getFile() != fileName:
            GPTRunningInstance = GPTRunning(fileName)

        # run gpt3 
        response = GPTRunningInstance.getCode(description)
        # response is a JSON need to fetch to code TODO

        GPTRunningInstance.getOutput

    # TODO:
    return render_template(...)


if __name__ == "__main__":
    app.run(debug=True)