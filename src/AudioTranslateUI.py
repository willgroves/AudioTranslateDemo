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

st.markdown('# Audio Translate Demo')
st.sidebar.markdown("# Main Menu")

st.write("Record some audio in Step 1 and exectute the model in Step 2. The model will transcribe or translate up to 30 seconds of audio.")
