"""
AudioTranslateUI.py

"""

import os
import pprint
from io import BytesIO
import whisper
import cattr
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from loguru import logger

st.set_page_config(layout="wide")

st.title('AudioTranslateUI')

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
st_audiorec = components.declare_component("st_audiorec", path=build_dir)

st.write("Record Audio")
# STREAMLIT AUDIO RECORDER Instance
val = st_audiorec()
# web component returns arraybuffer from WAV-blob
st.write('Audio data received in the Python backend will appear below this message ...')

if isinstance(val, dict):  # retrieve audio data
    with st.spinner('retrieving audio-recording...'):
        ind, val = zip(*val['arr'].items())
        ind = np.array(ind, dtype=int)  # convert to np array
        val = np.array(val)  # convert to np array
        sorted_ints = val[ind]
        stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
        wav_bytes = stream.read()

    # wav_bytes contains audio data in format to be further processed
    # display audio data as received on the Python side
    st.audio(wav_bytes, format='audio/wav')
    with open('audio.wav', 'wb') as f:
        f.write(wav_bytes)
    logger.info("wrote audio.wav")

st.write("Specify Language And Task")
language = st.text_input('input language', 'en')
task = st.text_input('task', 'transcribe')

model = None
st.write("available models are: {}".format(whisper.available_models()))

model_name = st.text_input('model name', 'base')
assigned_model_name = None

if st.button('Submit'):
    st.write('You clicked submit')

    # Do the task here
    if model is None or assigned_model_name != model_name:
        with st.spinner('loading whisper model...'):
            model = whisper.load_model(model_name)
            assigned_model_name = model_name

    import datetime

    start = datetime.datetime.utcnow()

    with st.spinner('running whisper model...'):
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio("audio.wav")
        audio = whisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # detect the spoken language
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions(task=task, language=language, fp16=False)
        result = whisper.decode(model, mel, options)

        st.write("time taken: {}".format((datetime.datetime.utcnow() - start).total_seconds()))

    # print the recognized text

    st.write("Output: \n" + pprint.pformat(cattr.unstructure(result)))
