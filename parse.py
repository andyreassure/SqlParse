import re

parenthesis = re.compile(r'\((?P<parenthesis>[^\(]+?)\)')
sql_prority_list = [
    re.compile(r'^select (?P<selects>.+?) from (?P<froms>.+) *(?:where (?P<wheres>.+?)) *(?:group by (?P<groups>.+?))? *(?:order by (?P<orders>.+?))?$'),
]
select_prority_list = [
    re.compile(r'^(?P<left>[^,]+),(?P<right>[^,]+)$'),
    re.compile(r'^(?P<oldname>.+) as (?P<newname>.+)$'),
    re.compile(r'^(?P<func>\w+)\((?P<arg>.+)\)|(?P<basicname>.+)$'),
]
from_prority_list = [
    re.compile(r'^(?P<left>[^,]+?),(?P<right>[^,]+)$'),
    re.compile(r'^(?P<filename>.+\.csv)$'),
]
where_prority_list = [
    re.compile(r'^(?P<left>[^,]+?) (?P<method>and|or) (?P<right>[^,]+)$'),
    re.compile(r'^(?P<dataname>[^,]+) (?P<method>==|!=|>|<) (?P<refvalue>)$')
]
group_prority_list = [
    re.compile(r'^(?P<left>[^,]+,)*(?P<right>[^,]+)$'),
]
order_prority_list = [
    re.compile(r'^(?P<left>[^,]+),(?P<right>[^,]+)$'),
    re.compile(r'^(?P<colname>.+?) (?P<da>desc|asc)?$')
]


class SqlParse(object):
    header = []
    data = []

    def PutData(self, header, data):
        self.header = header
        self.data = data
    
    def Execute(self, query):
        '''
        return a csvfile class
        '''
        something = self.SqlRoot(query)
        return something

    def SqlRoot(self, query):
        query = query.strip()
        res = sql_prority_list[0].match(query)
        if res:
            pass
        else:
            assert False, 'Wrong Sql format!'

    def SelectRoot(self, query):
        pass

    def FromRoot(self, query):
        '''
        return a filename list
        '''
        query = query.strip()
        res = parenthesis.search(query)
        while res:
            temp_filename = self.Execute(res.group('parenthesis'))
            query = query.replace(res.group(), temp_filename)
            res = parenthesis.search(query)
        return self.From1(query)

    def From0(self, query):
        query = query.strip()
        res = from_prority_list[0].match(query)
        
            

query = 'select A as mya, B as myb, avg(c) as f1, max(c) as f2 from (select * from 1.csv where iq > 100), 2.csv where name != "andy" and  (id == 13 or money > 1000) group by id, name, money order by A desc'

if __name__ == '__main__':
    dest = r'C:/Users/Admin/Desktop/Data'
    res = sql_prority_list[0].match(query)
    for item in res.groupdict().items():
        print(item)
    res = group_prority_list[0].match('id, name, money')
    print(res.groupdict())