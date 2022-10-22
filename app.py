from flask import Flask, request, g, render_template, redirect, session, flash

app = Flask(__name__, template_folder='templates')

# configurate the folder for csv files that uploaded by users
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UUPLOAD_FOLDER

@app.route('/', methods = ['POST','GET'])
def mainPage():
    if request.method == 'POST':
        # TODO: description = request
        # TODO: file = request 

        fileName = file.filename
        
        # TODO: initialize some information of the dataframe

        # TODO: run gpt3 

        # TODO: show code

        # TODO: show figure 
    # TODO:
    return render_template(...)

if __name__ == "__main__":
    app.run(debug=True)