import pandas as pd

from train.train_ds import train_dataset

class analyze_text:
    def __init__(self):
        pass

    def make_bow(self):
        pass


class train_text:
    def __init__(self):
        pass

    def append_to_ds(self, speech, appn, options=None):
        td = train_dataset()
        df = pd.DataFrame([[speech, appn, options]])
        td.write_to_ds(df)

