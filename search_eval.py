import math
import sys
import time

import metapy
import pytoml


def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate.

    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index. You can ignore this, unless
    you need to load a ForwardIndex for some reason...
    """
    return metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)

    cfg = sys.argv[1]
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker(cfg)
    ##ev = metapy.index.IREval(cfg)

    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query_cfg = cfg_d['query-runner']
    if query_cfg is None:
        print("query-runner table needed in {}".format(cfg))
        sys.exit(1)

    top_k = 100
    query_path = query_cfg.get('query-path', 'queries.txt')
    query_start = query_cfg.get('query-id-start', 0)
    query_num = int(sys.argv[3])

    print('Running queries')
    with open(query_path) as query_file:
        for line in query_file:
            query = metapy.index.Document()
            query.content(line.strip())
            res_num = 1
            for doc in ranker.score(idx, query, top_k):
                docnum = idx.metadata(doc[0].get('name'))
                print"{}\t_\t{}\t{}\t{}\tMeTA".format( query_num, docnum,res_num, doc[1]))
                res_num +=1
            query_num +=1
