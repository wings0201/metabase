#!/usr/bin/python

import sys
import csv


def load_data(filename):
    data = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter=',')

        count = 0
        for row in reader:
            if str.startswith(row[0], '--'):
                continue
            if count == 0:
                header = row
            else :
                data.append(row)
            count+=1

    return [header, data]


def build_sql_tempalte(tablename, cols):
    tmpl = 'insert into ' + tablename + ' ('
    value = ' values ('
    i = 0
    for col in cols:
        if i > 0:
            tmpl += ','
            value += ','
        i += 1
        tmpl += '`' + col + '`'
        value += '{' + str(i) + '}'
    return tmpl + ")" + value + ")"


if len(sys.argv) != 2:
    print 'usage: python import.py <data filename> <sql tablename>'


tablename = 'Transactions' #sys.argv[2]

[header, data] = load_data(sys.argv[1])

sqls = []

sqlTemplate = build_sql_tempalte(tablename, header)
print sqlTemplate


#for row in data:
#    sql = 'insert into ' + tablename + ' (' + ') values (' + ')'
