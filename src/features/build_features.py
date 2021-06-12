import pandas as pd
import numpy as np
import os
import sys

cwd = os.getcwd()
PROJECT_PATH = cwd.split("quince_assignment")[0] + 'quince_assignment'
sys.path.insert(0, PROJECT_PATH)


class FeatureBuild:
    def __init__(self, input_path):
        self.input_path = input_path
        self.event_data = None

    def load_data(self):
        self.event_data = pd.read_csv(self.input_path, compression="gzip")
        self.event_data['event_time'] = pd.to_datetime(self.event_data['event_time'], format="%Y-%m-%d %H:%M:%S")
        return self

