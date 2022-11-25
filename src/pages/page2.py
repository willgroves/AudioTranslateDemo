"""
AudioTranslateUI.py

"""

import os
import pprint
import datetime
from io import BytesIO
import whisper
import cattr
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from loguru import logger

st.set_page_config(layout="wide")
st.sidebar.markdown("# Step 1: Record Audio")

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
st_audiorec = components.declare_component("st_audiorec", path=build_dir)

st.write("Step 1: Record Audio (will transcribe or translate up to 30 seconds of audio):")
# STREAMLIT AUDIO RECORDER Instance
val = st_audiorec()
# web component returns arraybuffer from WAV-blob
st.write('Audio data received in the backend will appear below this message once transferred:')

if isinstance(val, dict):  # retrieve audio data
    with st.spinner('Retrieving audio-recording...'):
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

