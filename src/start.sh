#!/bin/bash

streamlit run --server.port 8080  --server.enableWebsocketCompression=false --server.enableCORS false --server.enableXsrfProtection false AudioTranslateUI.py
