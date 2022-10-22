from asyncore import file_dispatcher
from weakref import finalize
from .gpt3 import setOpenai, Example, GPT
import pandas as pd
class GPTRunning:
    def __init__(self, filePath):
        self.gpt = GPT()
        self.filePath = filePath
        self.count = 0

    def columns(self):
        df = pd.read(self.filePath)
        return list(df.columns)

    def getResponse(self, prompt):
        finalPrompt = ""
        if self.count == 0:
            columnsPromt = str(self.filePath) + ', columns = ' +str(self.columns())
            initPrompt = '''
            Using Python Pandas
            Using Matplotlib
            '''
            filePrompt = 'create DataFrame for "' + str(self.filePath) + '" file \n'

            finalPrompt = columnsPromt + initPrompt + filePrompt + prompt

            
        else:
            finalPrompt = prompt
        
        self.count += 1
        return self.gpt.get_top_reply(finalPrompt)
        
    
