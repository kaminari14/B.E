import pandas as pd
from reusables import pandas_reusables as pr

class train_dataset():
    def __init__(self):
        pass

    def write_to_ds(self, df):
        '''
        write a new row to the dataset
        :param df: pandas dataset to be written to the file
        :return: None
        '''
        fp = "../Datasets/commands.csv"
        pr.add_row(df,fp)
        self._print_ds(fp)

    def _print_ds(self, filepath):
        '''
        print the last 10 rows from the dataset
        :param filepath: file path to the csv file that contains the dataset
        :return: None
        '''
        pr.print_tail(filepath)
        #retrain?