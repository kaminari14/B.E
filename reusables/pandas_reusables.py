import csv
import pandas as pd

def add_row(df, filepath):
    try:
        df.to_csv(filepath, mode="a", header=False, index=False, line_terminator="\n")
    except Exception as e:
        print(e)


def print_tail(filepath):
    df = pd.read_csv(filepath)
    print(df.tail(10))

