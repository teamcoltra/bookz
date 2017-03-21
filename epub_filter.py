
import os
import collections

dir_name = ['.']
extension = ['.txt']
formats = ['epub']
servers = ['!Ook', '!vadi']
Book = collections.namedtuple('Book', ['server', 'author', 'series', 'name'])
variables = {}

for item in os.listdir(dir_name[0]):
    if item.endswith(extension[0]):
        file_name = os.path.abspath(item)
        for line in open(file_name):
            if any(format in str(line) for format in formats) and any(server in str(line) for server in servers):
                a = line.split('-')
                if len(a) == 2:
                    b = a[0].split(' ')
                    b = list(filter(None, b))
                    string = 'server:' + str(b[0]) + '|' + 'author:' + str(b[1])
                    for i in range(2, len(b)):
                        string += ' ' + str(b[i])
                    string += '|' + 'name:'
                    c = a[1].split('::')
                    string += str(c[0]).strip()
                    print(string)

                    current = string.split('|')
                    server = current[0].split(':')
                    author = current[1].split(':')
                    name = current[2].split(':')

                    Book(server[1], author[1], '', name[1])

                elif len(a) == 3:
                    b = a[0].split(' ')
                    b = list(filter(None, b))
                    string = 'server:' + str(b[0]) + '|' + 'author:' + str(b[1])
                    for i in range(2, len(b)):
                        string += ' ' + str(b[i])
                    string += '|' + 'series:' + str(a[1]).strip() + '|' + 'name: '
                    c = a[2].split('::')
                    string += str(c[0]).strip()
                    print(string)

                    current = string.split('|')
                    server = current[0].split(':')
                    author = current[1].split(':')
                    series = current[2].split(':')
                    name = current[3].split(':')

                    Book(server[1], author[1], series[1], name[1])

print(f"Book = {Book!r}")
