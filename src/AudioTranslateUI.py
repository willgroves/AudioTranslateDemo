"""
AudioTranslateUI.py

"""

import streamlit as st

st.set_page_config(layout="wide")

st.markdown('# Audio Translate Demo')
st.sidebar.markdown("# Main Menu")

st.write("Record some audio in Step 1 and exectute the model in Step 2. The model will transcribe or translate up to 30 seconds of audio.")
