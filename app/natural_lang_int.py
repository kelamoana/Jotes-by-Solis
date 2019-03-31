# natural_lang_int.py


# import app.long_speech_to_text

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import requests

def natural_language_api(text):
    client = language.LanguageServiceClient()

    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document).entities
    lst = []

    for entity in entities:
        lst.append(entity.name)
    return lst

def wikipedia(lst):
    S = requests.Session()
    resources = []
    URL = "https://en.wikipedia.org/w/api.php"
    for word in lst:
        SEARCHTERM = word

        PARAMS = {
            'action': "opensearch",
            'search': SEARCHTERM,
            'limit': 1,

            'format': "json"
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        if DATA[3]!=[]:
            resources.append(DATA[3][0])
    return resources



if __name__ == '__main__':
    file = 'gs://petersaudiofiles/bettersong.flac'
    #print(natural_language_api(long_speech_to_text.transcribe_gcs(file)))
