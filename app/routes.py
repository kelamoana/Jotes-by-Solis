from app import app
from flask import render_template, redirect, url_for
from app.oxfordapi import create_def_dict
from app.long_speech_to_text import transcribe_gcs
from app.natural_lang_int import natural_language_api


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    file_name = 'gs://petersaudiofiles/bettersong.flac'
    transcription = ''
    transcription = transcribe_gcs(file_name)
    keywords = []
    resources = []
    words = natural_language_api(transcription)
    
    for word in words:
        if len(keywords) == 12:
            break
        try:
            keywords.append(create_def_dict(word['name']))
            if word['wiki'] != None:
                resources.append(word['wiki'])
        except:
            continue

    return render_template('index.html', keywords=keywords, transcription=transcription, resources=resources)

@app.route('/about')
def about():
    return render_template('about.html')