from reusables import pandas_reusables as pr
import pandas as pd
from text_process.process_text import train_text
import main.subpr_exec as se

class action:
    def __init__(self):
        self.apps = pd.read_csv("../apps.csv")
        self.appnames = [names for names in self.apps['app']]

    def _init_appdata(self):
        self.apps = pd.read_csv("../apps.csv")
        self.appnames = [names for names in self.apps['app']]

    def process_command(self, mode, speech):
        if mode == "train":
            app = input("what is the application name?")
            if app not in self.appnames:
                appcommand = input("application not found in the applications list. Enter the OS command for the application")
                new_app = True
            else:
                appcommand = self.apps.loc[self.apps['app'] == app, 'command'].iloc[0]
                new_app = False
            extra = input("options with the command")
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
            tr = input("Do you want to train the DS(Y/N)?")
            if tr == "Y":
                t = train_text()
                t.append_to_ds(speech, app, extra)
                if new_app:
                    pr.add_row(pd.DataFrame([[app, appcommand]]),"../apps.csv")
                self._init_appdata()



x = action()
x.process_command("train", input("give a verbal command"))






