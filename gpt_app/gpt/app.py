from flask import Flask, request
from flask_cors import CORS, cross_origin
from gpt3 import GPTRunning, setOpenai

setOpenai("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")

app = Flask(__name__, template_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# configurate the folder for csv files that uploaded by users
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/', methods=['GET'])
# def index():
#   return {'name': 'asda'}


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def mainPage():
  response = {}
  if request.method == 'POST':
    uploadFile = request.files['csvFile']
    instruction = request.form['instruction']
    fileName = uploadFile.filename
    uploadFile.save(fileName)
    GPTRunningInstance = GPTRunning(fileName)

    # if GPTRunningInstance.getFile() == "" or GPTRunningInstance.getFile() != fileName:
    #   GPTRunningInstance = GPTRunning(fileName)

    # run gpt3
    response = GPTRunningInstance.getCode(instruction)
    # # response is a JSON need to fetch to code TODO
    return (response)
  return response


if __name__ == "__main__":
  app.run(debug=True)
