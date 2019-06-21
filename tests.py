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
        expected_total = 24250
        data_filtered, total = self.data_process.filter_data()
        self.assertEqual(expected_data, data_filtered)
        self.assertEqual(expected_total, total)

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

    def test_leases_between_dates(self):
        expected_data = [
            {
                'Property Name': 'Property1',
                'Property Address [1]': 'Addr1_1',
                'Property  Address [2]': 'Addr2_1',
                'Property Address [3]': 'Addr3_1',
                'Property Address [4]': 'Addr4_1',
                'Unit Name': 'Unit1',
                'Tenant Name': 'Tenant1',
                'Lease Start Date': '01/01/2000',
                'Lease End Date':'01/01/2010',
                'Lease Years': '10',
                'Current Rent': '12345',
            },
            {
                'Property Name': 'Property2',
                'Property Address [1]': 'Addr1_2',
                'Property  Address [2]': 'Addr2_2',
                'Property Address [3]': 'Addr3_2',
                'Property Address [4]': 'Addr4_2',
                'Unit Name': 'Unit2',
                'Tenant Name': 'Tenant2',
                'Lease Start Date': '30/01/2004',
                'Lease End Date':'29/01/2029',
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
                'Lease Start Date': '26/07/2007',
                'Lease End Date':'25/07/2032',
                'Lease Years': '25',
                'Current Rent': '12000',
            },
            {
                'Property Name': 'Property7',
                'Property Address [1]': 'Addr1_7',
                'Property  Address [2]': '',
                'Property Address [3]': '',
                'Property Address [4]': '',
                'Unit Name': 'Unit7',
                'Tenant Name': 'Tenant1',
                'Lease Start Date': '31/03/2000',
                'Lease End Date':'30/03/2030',
                'Lease Years': '30',
                'Current Rent': '10000',
            },
        ]
        leases = self.data_process.leases_between_dates()
        self.assertEqual(leases, expected_data)


