# long_speech_to_text.py


def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.FLAC, sample_rate_hertz=8000,
                                     language_code='en-US')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=150)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    ret_str = ''

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        ret_str += str(result.alternatives[0].transcript)

    return ret_str





if __name__ == '__main__':
    s = transcribe_gcs('gs://petersaudiofiles/bettersong.flac')

    print(s)
