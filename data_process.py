import csv
import datetime


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
        data_filtered = [x for x in self._data if x['Lease Years'] == '25']
        return data_filtered, sum([int(x['Current Rent']) for x in data_filtered])

    def generate_count(self):
        counts = {}
        for item in self._data:
            counts[item['Tenant Name']] = counts.get(item['Tenant Name'], 0) + 1

        return counts

    def leases_between_dates(self):
        start_date = datetime.datetime(1999, 6, 1)
        end_date = datetime.datetime(2007,8,1)
        data_filtered = []
        for item in self._data:
            cur_date = datetime.datetime.strptime(item['Lease Start Date'], '%d-%b-%y')
            if cur_date >= start_date and cur_date <= end_date:
                data_filtered.append(item)

        return data_filtered
