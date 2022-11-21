#!/bin/bash

# create submodule in this directory

# Only do this once:

if [ "$DOONCE" == "1" ]; then
  git submodule add https://github.com/stefanrmmr/streamlit_audio_recorder.git contrib_streamlit_audio_recorder
fi
# update submodule only do this if submodule is not already populated

git submodule update --init --recursive


if [ "$DOONCE" == "1" ]; then
  ln -s contrib_streamlit_audio_recorder/st_audiorec st_audiorec
fi