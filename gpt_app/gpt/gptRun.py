from weakref import finalize
from gpt3 import  Example, GPT
import pandas as pd
import os, shutil

class GPTRunning:
    def __init__(self, filePath):
        self.gpt = GPT()
        self.filePath = filePath
        self.count = 0

    def getFile(self):
        return self.filePath

    def columns(self):
        df = pd.read_csv(self.filePath)
        return list(df.columns)

    def setPrompt(self, prompt):
        finalPrompt = ""
        if self.count == 0:
            columnsPromt = 'Table ' + str(self.filePath) + ', columns = ' +str(self.columns())
            initPrompt = '''
            Using Python Pandas
            Using Matplotlib
            '''
            filePrompt = 'create DataFrame for "' + str(self.filePath) + '" file \n'

            finalPrompt = columnsPromt + initPrompt + filePrompt + prompt

        else:
            finalPrompt = prompt

        self.prompt = finalPrompt

    def getCode(self, prompt):
        finalPrompt = ""
        if self.count == 0:
            columnsPromt = 'Table ' + str(self.filePath) + ', columns = ' +str(self.columns())
            initPrompt = '''
            Using Python Pandas
            Using Matplotlib
            '''
            filePrompt = 'create DataFrame for "' + str(self.filePath) + '" file \n'

            finalPrompt = columnsPromt + initPrompt + filePrompt + prompt

        else:
            finalPrompt = prompt

        self.count += 1

        return self.gpt.submit_request(finalPrompt)
        
    def getOutput(self, code):
        if self.count == 0:
            folder = "data/output"
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            file = open("data/output/runGPTCode.py",'w')
        else:
            file = open("data/output/runGPTCode.py",'a')
        idx = code['choices'][0]['text'].find("\n\'\'\'")
        if idx == -1:
            idx = code['choices'][0]['text'].find("\n\n\"\"\"")
        parsingCode = code['choices'][0]['text'][idx+5:]
        file.write(parsingCode)
        file.close()

        import data.output.runGPTCode as GPTCode
        GPTCode.main()
        
