from elasticsearch import Elasticsearch, helpers

partial_index = "cs499-subdocuments"
full_index = "cs499-fulldocuments"

def new_search_engine():
    es = Elasticsearch('http://localhost:9200', verify_certs=False)
    return es

def index_documents(es, subdocuments):
    full_document = {
        "Filename": subdocuments[0]["Filename"],
        "Visual": "",
        "Audio": "",
    }
    for i in range(len(subdocuments)):
        # full_document["Visual"] = full_document["Visual"] + subdocuments[i]["Visual"] + " "
        full_document["Audio"] = full_document["Audio"] + subdocuments[i]["Audio"]

    res = helpers.bulk(es, subdocuments, index=partial_index)
    # TODO: error check res
    res = es.index(index=full_index, document=full_document)
    return res

def search_documents(es, query, get_full_document):
    index_name = ""
    if get_full_document:
        index_name = full_index
    else:
        index_name = partial_index
    res = es.search(index=index_name, track_total_hits=True, query={"match": {
        "Audio": {"query": query, "operator": "OR"},
        # "Visual": {"query": query, "operator": "OR"},
        }})
    
    return res
