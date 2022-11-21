#!/bin/bash

# This script is used to build the docker image for the translation demo using OpenAI Whisper

if [ "$UPLOAD" == "1" ]; then
  gcloud auth configure-docker  us-east1-docker.pkg.dev
fi

docker build -t us-east1-docker.pkg.dev/gcloudsdk-on-wmm/gdocker/audiotranslatedemo:v20221121a .

if [ "$UPLOAD" == "1" ]; then
  docker push us-east1-docker.pkg.dev/gcloudsdk-on-wmm/gdocker/audiotranslatedemo:v20221121a
fi
