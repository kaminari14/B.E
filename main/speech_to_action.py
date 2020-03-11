from reusables import pandas_reusables as pr
import pandas as pd
from text_process.process_text import train_text
import main.subpr_exec as se
from text_process.process_text import analyze_text

class action:
    def __init__(self):
        self.apps = pd.read_csv("../apps.csv")
        self.app_dict = {names: apps for names,apps in zip(self.apps['app'], self.apps['command'])}
        self.df = pd.read_csv("../Datasets/commands.csv")
        self.text_analyzer = analyze_text()
        self.text_analyzer.train_model(self.df)

    def _init_appdata(self):
        '''
        Reinitialize pandas dataframe with the new data in the dataset.

        :return:
        '''
        self.df = pd.read_csv("../Datasets/commands.csv")
        self.apps = pd.read_csv("../apps.csv")
        self.app_dict = {names: apps for names, apps in zip(self.apps['app'], self.apps['command'])}
        self.text_analyzer.train_model(self.df)


    def process_command(self, mode, speech):
        if mode == "train":  #make changes according to app_dict
            self.train(speech)
        if mode == "run":
            preds = self.text_analyzer.predict(speech)
            preds[0] = self.app_dict[preds[0]]
            print(" ".join(preds))
            exec_ = input("is this the command you want me to execute(Y/N)")
            if exec_ == "Y":
                self._get_output(preds[0], preds[1])
            else:
                print("Help me learn")
                self.train(speech)


    def train(self, speech):
        app = input("what is the application name?")
        if app not in self.app_dict.keys():
            appcommand = input(
                "application not found in the applications list. Enter the OS command for the application")
            new_app = True
        else:
            appcommand = self.app_dict[app]
            new_app = False
        extra = input("options with the command")
        self._get_output(appcommand, extra)
        tr = input("Do you want to train the DS(Y/N)?")
        if tr == "Y":
            t = train_text()
            t.append_to_ds(speech, app, extra)
            if new_app:
                pr.add_row(pd.DataFrame([[app, appcommand]]), "../apps.csv")
                self._init_appdata()

    def _get_output(self, appcommand, extra):
        return_code, pid, output, err = se.exec_command(appcommand, extra.split())
        if return_code != 0:
            print("Non Zero return code")
            print("ERRRR:")
            print(err)
        elif err:
            print("ERRR:")
            print(err)
            print("OUTPUT")
            print(bytes(output).decode("utf-8"))
        else:
            print("OUTPUT")
            print(bytes(output).decode("utf-8"))

x = action()
x.process_command("run", input("give a verbal command"))






