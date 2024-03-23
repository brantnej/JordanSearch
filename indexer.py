from elasticsearch import Elasticsearch, helpers

partial_index = "cs499-subdocuments-final"
full_index = "cs499-fulldocuments-final"

image_boost = 2

def new_search_engine():
    es = Elasticsearch('http://localhost:9200', verify_certs=False)
    return es

def index_documents(es, subdocuments):
    full_document = {
        "Filename": subdocuments[0]["Filename"],
        "Image": " ".join([i["Image"] for i in subdocuments]),
        "Audio": " ".join([i["Audio"] for i in subdocuments])
    }

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
    res = es.search(index=index_name, track_total_hits=True, query={"multi_match": {
        "query": query,
        "fields": ["Image^" + str(image_boost), "Audio"]
        }})
    return res
