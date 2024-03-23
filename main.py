from conversions import *
from indexer import *
from audio_parser import *
from image_parser import *
import math
import sys

path = './input'

es = new_search_engine()

if not es.ping():
    print("ElasticSearch is not running!")
    exit()

if len(sys.argv) > 1 and ("-p" in sys.argv or "--parse" in sys.argv):

    print("Initializing Models...")

    image_model = new_image_model()
    audio_model = new_audio_model()

    print("Beginning Indexing...")

    for file_name in os.listdir(path):
        audio_file = extract_audio(path + '/' + file_name)
        phrases = parse_file(audio_model, audio_file)

        documents = []

        for phrase in phrases:
            if "result" in phrase:
                timestamp = seconds_to_timestamp(math.ceil(float(phrase["result"][0]["start"])))
                image = extract_image(file_name=path + '/' + file_name, timestamp=timestamp)
                res = detect_objects(image_model, image)
                subdocument = {
                    "Timestamp": phrase["result"][0]["start"],
                    "Audio": phrase["text"],
                    "Filename": file_name,
                    "Image": " ".join([i['name'] for i in res])
                }
                documents.append(subdocument)
    
        index_documents(es, documents)

    clean_up_audio()
    clean_up_image()

    print("Search engine ready!")

get_full_document = False
if "-f" in sys.argv or "--full" in sys.argv:
    get_full_document = True

while True:
    query = input("Enter a query:")
    res = search_documents(es, query, get_full_document=get_full_document)
    output = [{"Timestamp": i["_source"]["Timestamp"],
               "Audio": i["_source"]["Audio"],
               "Image": i["_source"]["Image"],
               "File": i["_source"]["Filename"]}
              for i in res['hits']['hits']]
    for i in range(len(output)):
        print("#" + str(i + 1) + ": " + str(output[i]))