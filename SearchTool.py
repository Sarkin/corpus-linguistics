#coding=utf-8

from __future__ import print_function
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

index_path = './index'

ix = open_dir(index_path)

while True:
    request = ''
    try:
        request = raw_input('Insert request: ')
    except Exception as e:
        print(e.message)

    if request == 'exit':
        break
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(request.decode(encoding='utf-8'))
        results = searcher.search(query)
        for i in range(min(len(results), 10)):
            print(i, results[i]['title'])
