import pandas as pd
import spacy
from train.train_ds import train_dataset
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.multioutput import MultiOutputClassifier

class analyze_text:
    def __init__(self):
        pass

    def _tfidftransformation(self, df):
        '''
        TFIDF transformation of the training DS
        :param df: the entire dataset
        :return: X_train. the vectorized and tranformed input training ds.
        '''
        pd.options.mode.chained_assignment = None
        nlp = spacy.load("en_core_web_sm")
        X = df["Speech"]
        self.vectoriser = TfidfVectorizer()
        X_train = self.vectoriser.fit_transform(X)
        print(X_train.shape)
        print(self.vectoriser.get_feature_names())
        print(X_train)
        return X_train

    def train_model(self, df):
        '''
        Train the model using liner SVC
        :param df: the entire ds
        :return: None
        '''
        training_ds = self._tfidftransformation(df)
        y = df[["app","options"]]
        y.fillna('', inplace=True)
        print(y)
        self.clf = MultiOutputClassifier(LinearSVC())
        self.clf.fit(training_ds, y)

    def predict(self, speech):
        '''
        predict using the trained model
        :param speech: the verbal command
        :return: [app, options] predictions
        '''
        test = [speech]
        test = self.vectoriser.transform(test)
        preds = self.clf.predict(test)
        return preds[0]



class train_text:
    def __init__(self):
        pass

    def append_to_ds(self, speech, appn, options=None):
        '''
        append new data to the training dataset
        :param speech: the verbal command
        :param appn: the pplication name
        :param options: the extra options to be ran with the command. Defaults to None.
        :return: None
        '''
        td = train_dataset()
        df = pd.DataFrame([[speech, appn, options]])
        td.write_to_ds(df)


'''
x= analyze_text()
x.train_model(pd.read_csv("../Datasets/commands.csv"))
print(x.predict("what processes are currently running?"))
'''


