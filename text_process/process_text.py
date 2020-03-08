import pandas as pd
import spacy
from train.train_ds import train_dataset

class analyze_text:
    def __init__(self):
        pass

    def make_bow(self):  #, df):
        pass
        #nlp = spacy.load("en_core_web_sm")
        #print(nlp.default.stop_words)


class train_text:
    def __init__(self):
        pass

    def append_to_ds(self, speech, appn, options=None):
        td = train_dataset()
        df = pd.DataFrame([[speech, appn, options]])
        td.write_to_ds(df)

