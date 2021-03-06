import math
import sys
import time
import metapy
import pytoml
import operator
from collections import OrderedDict
import shutil
import os.path

# sort the score of each query from high to low and choose the top 5
def sort_score(result_list,n,total):
    ret = [None]*total
    for i in range(total):
        if bool(result_list[i]):
          x = OrderedDict(sorted(result_list[i].items(), key=operator.itemgetter(1), reverse=True)[:n])
          ret[i]=list(x.keys())
    return ret

# implement metapy BM25 method
def load_ranker(cfg_file):
    return metapy.index.OkapiBM25(k1=2.5,b=0.75,k3=0.65)

# read queries, estimate them with the gathered review data and print the results
def process(reviews, word_num = 5):
    if os.path.exists('index'):
        shutil.rmtree('index')
    cfg = "config.toml"

    # create index & set configuration(including stop words)
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker(cfg)

    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query_cfg = cfg_d['query-runner']
    if query_cfg is None:
        print("query-runner table needed in {}".format(cfg))
        sys.exit(1)

    result_list = [None]*reviews
    
    # read queries
    top_k = 2
    query_path = query_cfg.get('query-path', 'queries.txt')
    query_start = query_cfg.get('query-id-start', 0)

    f = open('result.txt','w')
    doc = metapy.index.Document()
    query = metapy.index.Document()

    # calculate score for each query and store the assessment data
    print('Running queries')
    with open(query_path) as query_file:
        for query_num, line in enumerate(query_file):
            doc.content(line.strip())
            # filtrate stemming
            tok = metapy.analyzers.ICUTokenizer()
            tok.set_content(doc.content())
            tok = metapy.analyzers.Porter2Filter(tok)
            tokens = [token for token in tok]
            query.content(str(tokens[1]).strip())            
            results = ranker.score(idx, query, top_k)
            for x in results:
              if bool(result_list[int(x[0])]):
                result_list[int(x[0])].update({str(query.content()): x[1]})
              else:
                result_list[int(x[0])] = {str(query.content()): x[1]}
            a = "{}\t{}\t{}\n".format(query_num, query.content(), results)
            f.write(a)
    f.close()
    # detemine the top 5 as the results
    final_result = sort_score(result_list,word_num,reviews)
    return final_result

# main
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Wrong command")
        sys.exit(1)

    # get words number needed for each review level of a product
    word_num = sys.argv[1]
    process(int(word_num))
