import json
import requests


def build_url(word: str) -> str:
    language = 'en'

    return 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()


def json_dict(url: str) -> dict:
    app_id = '0401a21b'
    app_key = 'cd77a511e518552d24f1252234809f1a'
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    return eval(r.text)


def get_definition(json: dict) -> str:
    return json['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]


def define(word: str) -> str:
    url = build_url(word)
    json = json_dict(url)
    return get_definition(json)


def create_def_dict(word: str) -> dict:
    '''creates a dict, keys = word, definition'''
    return {'word': word, 'definition': define(word)}


def run() -> None:
    print(create_def_dict('apple'))
    while True:
        word = input('Input word or \'q\' to proceed: ')
        if word.lower() == 'q':
            break
        try:
            url = build_url(word)
            json = json_dict(url)
            definition = get_definition(json)
            print(f"\nDefinition of {word}:\n\n{definition}\n")
        except:
            print('\nWord not found in Oxford Dictionary. Try again.\n')
            continue


if __name__ == '__main__':
    run()
