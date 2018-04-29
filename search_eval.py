import math
import sys
import time

import metapy
import pytoml
import operator
from collections import OrderedDict

def sort_score(result_list,n,total):
    ret = [None]*total
    for i in range(total):
        if bool(result_list[i]):
	    x = OrderedDict(sorted(result_list[i].items(), key=operator.itemgetter(1), reverse=True)[:n])
            ret[i]=list(x.keys())
    return ret

def load_ranker(cfg_file):
    
    return metapy.index.OkapiBM25(k1=2.5,b=0.75,k3=0.65)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)

    cfg = sys.argv[1]
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker(cfg)

    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query_cfg = cfg_d['query-runner']
    if query_cfg is None:
        print("query-runner table needed in {}".format(cfg))
        sys.exit(1)

    result_list = [None]*20
    
    top_k = 2
    query_path = query_cfg.get('query-path', 'queries.txt')
    query_start = query_cfg.get('query-id-start', 0)

    f = open('result.txt','w')
    query = metapy.index.Document()
    print('Running queries')
    with open(query_path) as query_file:
        for query_num, line in enumerate(query_file):
            query.content(line.strip())
	    results = ranker.score(idx, query, top_k)
            for x in results:
	        if bool(result_list[int(x[0])]):
		    result_list[int(x[0])].update({str(query.content()): x[1]})
                else:
		    result_list[int(x[0])] = {str(query.content()): x[1]}
            a = "{}\t{}\t{}\n".format(query_num, query.content(), results)
            f.write(a)
    f.close()
    final_result = sort_score(result_list,5,20)
    
    for xx in range(20):
        if bool(final_result[xx]):
	    print("{}\t{}\t".format(xx+1,final_result[xx]))
	else:
	    print("{}\tNone".format(xx+1))
