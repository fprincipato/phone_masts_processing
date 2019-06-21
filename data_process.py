import csv


class DataProcess(object):
    def __init__(self, data_file_path):
        self._data_file_path = data_file_path

    def load_data_file(self):
        with open(self._data_file_path, 'r') as f:
            reader = csv.DictReader(f)
            self._data = [item for item in reader]

    def sort_data(self):
        return sorted(
            self._data,
            key=lambda x: float(x['Current Rent'])
        )

    def filter_data(self):
        return [x for x in self._data if x['Lease Years'] == '25']

    def generate_count(self):
        counts = {}
        for item in self._data:
            counts[item['Tenant Name']] = counts.get(item['Tenant Name'], 0) + 1

        return counts
