import unittest

from data_process import DataProcess


class TestDataProcess(unittest.TestCase):


    def setUp(self):
        self.data_process = DataProcess('./fixture.csv')
        self.data_process.load_data_file()

    def test_init_read(self):
        data_process = DataProcess('/path/to/file')
        self.assertEqual(
            data_process._data_file_path,
            '/path/to/file'
        )
    def test_load_data_file(self):
        expected_keys = [
            'Property Name', 'Property Address [1]', 'Property  Address [2]',
            'Property Address [3]', 'Property Address [4]',
            'Unit Name', 'Tenant Name', 'Lease Start Date',
            'Lease End Date', 'Lease Years', 'Current Rent',
        ]
        self.assertEqual(len(self.data_process._data), 7)
        self.assertEqual(list(self.data_process._data[0].keys()), expected_keys)

    def test_sort_data(self):
        sorted_data = self.data_process.sort_data()
        rents = [float(x['Current Rent']) for x in sorted_data]
        self.assertEqual(sorted(rents), rents)

    def test_filter_data(self):
        expected_data = [
            {
                'Property Name': 'Property2',
                'Property Address [1]': 'Addr1_2',
                'Property  Address [2]': 'Addr2_2',
                'Property Address [3]': 'Addr3_2',
                'Property Address [4]': 'Addr4_2',
                'Unit Name': 'Unit2',
                'Tenant Name': 'Tenant2',
                'Lease Start Date': '30-Jan-04',
                'Lease End Date':'29-Jan-29',
                'Lease Years': '25',
                'Current Rent': '12250',
            },
            {
                'Property Name': 'Property3',
                'Property Address [1]': 'Addr1_3',
                'Property  Address [2]': '',
                'Property Address [3]': '',
                'Property Address [4]': '',
                'Unit Name': 'Unit3',
                'Tenant Name': 'Tenant1',
                'Lease Start Date': '26-Jul-07',
                'Lease End Date':'25-Jul-32',
                'Lease Years': '25',
                'Current Rent': '12000',
            },
        ]
        data_filtered = self.data_process.filter_data()
        self.assertEqual(expected_data, data_filtered)

    def test_generate_count(self):
        expected_counts = {
            'Tenant1': 3,
            'Tenant2': 1,
            'Tenant3': 1,
            'Tenant4': 1,
            'Tenant6': 1,
        }
        counts = self.data_process.generate_count()
        self.assertEqual(expected_counts, counts)


