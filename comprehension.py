import csv

f = open('dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)

def date_to_tuple(date):
    return tuple([int(n) for n in date.split('/')])

types = [str, float, date_to_tuple, str, float, float, float, float, int]

l = [ { name: func(val) for name, func, val in zip(headers, types, row) } for row in rows ]

l_5 = l[:5]

f.close()
