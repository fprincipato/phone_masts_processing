import csv
import datetime
import argparse
import pprint


class DataProcess(object):

    def __init__(self, data_file_path, mode='all'):
        modes = {
            'section1': self.section_one,
            'section2': self.section_two,
            'section3': self.section_three,
            'section4': self.section_four,
            'all': self.all_sections
        }
        self._data_file_path = data_file_path
        self.load_data_file()
        modes[mode]()

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
            cur_start_date = datetime.datetime.strptime(item['Lease Start Date'], '%d-%b-%y')
            cur_end_date = datetime.datetime.strptime(item['Lease End Date'], '%d-%b-%y')
            if cur_start_date >= start_date and cur_start_date <= end_date:
                item['Lease Start Date'] = datetime.datetime.strftime(cur_start_date, '%d/%m/%Y')
                item['Lease End Date'] = datetime.datetime.strftime(cur_end_date, '%d/%m/%Y')
                data_filtered.append(item)

        return data_filtered

    def section_one(self):
        print('Section 1 ----------')
        for i in self.sort_data()[:5]:
            print(i)

    def section_two(self):
        print('Section 2 ----------')
        items, tot = self.filter_data()
        for i in items:
            print(i)

        print('Total: ', tot)

    def section_three(self):
        print('Section 3 ----------')
        pprint.pprint(self.generate_count())

    def section_four(self):
        print('Section 4 ----------')
        for i in self.leases_between_dates():
            print(i)

    def all_sections(self):
        self.section_one()
        self.section_two()
        self.section_three()
        self.section_four()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Process the csv data and output required stats')
    parser.add_argument('--mode', dest='mode', default='all', help='This program can be run in different mode. To only print the first 5 items from the csv sorted by Current rent use "section1". To only print a list of masts data for leases of 25 years use "section2". To only print a count of masts per tenants use "section3". To print stats of leases started between 1-Jun-99 and 31-Aug-07 use "section4". To print all stats use "all" (default)', choices=['all', 'section1', 'section2', 'section3', 'section4'])
    args = parser.parse_args()

    DataProcess('./Test.csv', mode=args.mode)

