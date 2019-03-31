# natural_lang_int.py


# import app.long_speech_to_text

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def natural_language_api(text):
    client = language.LanguageServiceClient()

    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document).entities
    lst = []

    for entity in entities:
        lst.append(entity.name)
    return lst


if __name__ == '__main__':
    file = 'gs://petersaudiofiles/bettersong.flac'
    print(natural_language_api(long_speech_to_text.transcribe_gcs(file)))
