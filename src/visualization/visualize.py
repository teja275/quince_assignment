import pandas as pd
import numpy as np
import os
import sys

cwd = os.getcwd()
PROJECT_PATH = cwd.split("quince_assignment")[0] + 'quince_assignment'
sys.path.insert(0, PROJECT_PATH)


class DataViz:
    def __init__(self, input_path):
        self.input_path = input_path
        self.event_data = None
        self.unique_items = None

    def load_data(self):
        self.event_data = pd.read_csv(self.input_path, compression="gzip")
        self.event_data['event_time'] = pd.to_datetime(self.event_data['event_time'], format="%Y-%m-%d %H:%M:%S")
        return self

    def data_stats(self):
        self.unique_items = self.event_data.nunique().to_dict()
        print(f"Event data has {self.event_data.shape[0]} rows and {self.event_data.shape[1]} columns")
        print(f"There are ")



