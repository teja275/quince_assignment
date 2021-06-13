import pandas as pd
import numpy as np
import os
import sys

cwd = os.getcwd()
PROJECT_PATH = cwd.split("quince_assignment")[0] + 'quince_assignment'
sys.path.insert(0, PROJECT_PATH)


class DataLoader:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.event_data = None
        self.session_data = None
        self.user_data = None

    def load_event_data(self):
        self.event_data = pd.read_csv(f"{PROJECT_PATH}/src/data/{self.input_file_name}", compression="gzip")
        self.event_data['event_time'] = pd.to_datetime(self.event_data['event_time'], format="%Y-%m-%d %H:%M:%S")
        return self

    def create_session_data(self):
        

