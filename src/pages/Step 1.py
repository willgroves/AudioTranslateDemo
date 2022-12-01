"""
AudioTranslateUI.py

"""

import os

import streamlit as st
from audio_recorder_streamlit import audio_recorder
from loguru import logger

st.set_page_config(layout="wide")
st.sidebar.markdown("# Step 1: Record Audio")

st.write("Step 1: Record Audio (will transcribe or translate up to 30 seconds of audio):")

audio_bytes = audio_recorder()

# web component to play audio
st.write('Audio data received in the backend will appear below this message once transferred:')

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    with open('audio.wav', 'wb') as f:
        f.write(audio_bytes)
    logger.info("wrote audio.wav")

