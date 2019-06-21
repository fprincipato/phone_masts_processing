import csv


class DataProcess(object):
    def __init__(self, data_file_path):
        self._data_file_path = data_file_path

    def load_data_file(self):
        with open(self._data_file_path, 'r') as f:
            reader = csv.DictReader(f)
            self._data = [item for item in reader]
