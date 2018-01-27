import re
import sys
import os


class CsvFile:
    name = ''
    header = []
    data = []

    def __init__(self, url=None, sep=',', header=True):
        if url:
            if not os.path.exists(url):
                assert False, "File not exists"
            self.name = os.path.basename(url)
            with open(url, mode='r') as file:
                for line in file:
                    if header:
                        self.header = re.split(sep, line)
                        header = False
                    self.data.append(re.split(sep, line))
            self.Str2Num()

    def Str2Num(self):
        for line in self.data:
            for index in range(len(line)):
                if re.match(r'(?:[0-9]+(?:\.[0-9]+(?:E-?[0-9]+)?)?)', line[index]):
                    line[index] = float(line[index])

    def Num2Str(self):
        for line in self.data:
            for index in range(len(line)):
                if isinstance(line[index], float):
                    line[index] = str(line[index])
    
    def GenReport(self, url):
        self.Num2Str()
        with open(url, mode='w') as csvfile:
            csvfile.write(','.join(self.header) + '\n')
            for line in self.data:
                csvfile.write(','.join(line) + '\n')
        self.Str2Num()

    def PutData(self, name, header, data):
        self.name = name
        self.header = header
        self.data = data

    
class CsvSql:
    '''to create a dict tree for process data'''
    keywords = ["select", "from", "join", "where", "group by", "order by"]
    global_sep = ","

    def Root(self, sql):
        sqldict = dict()
        sqldict['selects'] = self.selects(sql)
        sqldict['froms'] = self.selects(sql)
        sqldict['joins'] = self.joins(sql)
        sqldict['wheres'] = self.wheres(sql)
        sqldict['groups'] = self.groups(sql)
        sqldict['orders'] = self.orders(sql)
        return sqldict

    def selects(self, sql):
        sql = re.match('select *(?P<cols>.+?) *from').group('cols')
        seldict = self.select0(sql)
        return seldict

    def select0(self, sql):
        sql = sql.strip()
        list0 = []
        subsql = ''
        depth = 0
        for char in sql + ',':
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                if depth < 0:
                    assert False, 'Parse error'
            if char == ',' and depth == 0:
                list0.append(self.select1(subsql))
                subsql = ''
            else:
                subsql += char

    def select1(self, sql):
        sql = sql.strip()
        subdict = dict()
        if re.match(r'(?P<colname>.+?) *(as) *(?P<alias>.+?)'):
            subdict['colname'] = 

    def froms(self, sql):
        pass

    def joins(self, sql):
        pass
    
    def wheres(self, sql):
        pass

    def groups(self, sql):
        pass

    def orders(self, sql):
        pass


class DataFactory:
    pass


if __name__ == "__main__":
    query = "select * from 1.csv, (select wage as income from 2.csv) where name != \"andy\" order by name >> a.csv"
    print(query)