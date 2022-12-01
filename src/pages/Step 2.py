"""
AudioTranslateUI.py

"""

import datetime
import pprint

import cattr
import streamlit as st
import whisper

st.set_page_config(layout="wide")

st.sidebar.markdown("# Step 2: Specify Language And Task")

st.write("Step 2: Specify Language And Task")
language = st.text_input('Input language (use language codes, e.g. "en" for English)', 'en')
task = st.text_input('Task (choices: transcribe, translate)', 'transcribe')

model = None

model_name = st.text_input('Model name (default: base, Available models are: {}'.format(whisper.available_models()), 'base')
assigned_model_name = None

st.write("Step 3: Run the Model")
if st.button('Run Model'):
    #st.write('You clicked submit')

    # Do the task here
    if model is None or assigned_model_name != model_name:
        with st.spinner('Loading whisper model (this may take up to 1 minute when a model is loaded for the first time)...'):
            model = whisper.load_model(model_name)
            assigned_model_name = model_name

    start = datetime.datetime.utcnow()

    with st.spinner('Running whisper model on the audio...'):
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

        st.write("Time taken: {} s".format((datetime.datetime.utcnow() - start).total_seconds()))

    # print the recognized text
    st.write("Result: " + pprint.pformat(cattr.unstructure(result)))
