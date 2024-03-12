from mp4_to_wav import *
from indexer import *
from audio_parser import *
import sys

path = './input'

es = new_search_engine()

if not es.ping():
    print("ElasticSearch is not running!")
    exit()

if len(sys.argv) > 1 and (sys.argv[1] == "-p" or sys.argv[1] == "-parse"):

    print("Beginning Indexing...")

    model = new_model()

    for file_name in os.listdir(path):
        audio_file = convert_file(path + '/' + file_name)
        phrases = parse_file(model, audio_file)
        clean_up_audio_converter()

        documents = []

        for phrase in phrases:
            subdocument = {
                "Timestamp": phrase["result"][0]["start"],
                "Audio": phrase["text"],
                "Filename": file_name,
            }
            documents.append(subdocument)

        index_documents(es, documents)

    print("Search engine ready!")

while True:
    query = input("Enter a query:")
    res = search_documents(es, query, get_full_document=False)
    output = [{"Timestamp": i["_source"]["Timestamp"],
               # "Audio": i["_source"]["Audio"],
               "File": i["_source"]["Filename"]}
              for i in res['hits']['hits']]
    for i in range(len(output)):
        print("#" + str(i + 1) + ": " + str(output[i]))