#!/bin/bash



rm -rf contrib_streamlit_audio_recorder st_audiorec

git clone https://github.com/stefanrmmr/streamlit_audio_recorder.git contrib_streamlit_audio_recorder

ln -s contrib_streamlit_audio_recorder/st_audiorec st_audiorec
