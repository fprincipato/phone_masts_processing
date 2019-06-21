import unittest

from data_process import DataProcess


class TestDataProcess(unittest.TestCase):

    def test_init_read(self):
        data_process = DataProcess('/path/to/file')
        self.assertEqual(
            data_process._data_file_path,
            '/path/to/file'
        )
    def test_load_data_file(self):
        data_process = DataProcess('./Test.csv')
        data_process.load_data_file()
        expected_keys = [
            'Property Name', 'Property Address [1]', 'Property  Address [2]',
            'Property Address [3]', 'Property Address [4]',
            'Unit Name', 'Tenant Name', 'Lease Start Date',
            'Lease End Date', 'Lease Years', 'Current Rent',
        ]
        self.assertEqual(len(data_process._data), 42)
        self.assertEqual(list(data_process._data[0].keys()), expected_keys)

    def test_sort_data(self):
        data_process = DataProcess('./Test.csv')
        data_process.load_data_file()
        sorted_data = data_process.sort_data()
        rents = [float(x['Current Rent']) for x in sorted_data]
        self.assertEqual(sorted(rents), rents)

