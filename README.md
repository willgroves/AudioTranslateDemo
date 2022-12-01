
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="image.png" alt="Logo">
  </a>

<h3 align="center">Audio Translate Demo</h3>

  <p align="center">
 ·
    <a href="https://audio.nyctaxi.me/">View Live Demo</a>
    ·
    <a href="https://github.com/willgroves/AudioTranslateDemo/issues">Report Bug</a>
    ·
    <a href="https://github.com/willgroves/AudioTranslateDemo/issues">Request Feature</a>
·
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

* AudioTranslateDemo is a demo of the [OpenAI Whisper](https://github.com/openai/whisper) transcription and translation model released and discussed in [this paper](https://cdn.openai.com/papers/whisper.pdf). It is a simple web frontend that allows you to upload an audio file and translate it to text. The text is then translated to another language and spoken back to you.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Motivation

This repository demonstrates deployment of a Streamlit application to the Google Cloud Platform. In particular, it exercises several features:
* [OpenAI Whisper](https://github.com/openai/whisper) transcription and translation model in a single deep learning model (unlike the traditional two phase system of Automatic Speech Recognition and Translation)
* [Cloud Run](https://cloud.google.com/run) for hosting the application in a way that can facilitate scale to zero (no resources are consumed if the service is not being actively used)
* [Streamlit](https://streamlit.io/) for the web frontend
* [Docker](https://www.docker.com/) for containerization
* [Google Cloud Build](https://cloud.google.com/build) for building the container and deploying to Cloud Run
* [Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry) for storing the container image

## Getting Started

To try things out, you can use the live demo at https://audio.nyctaxi.me/. If deploying another instance is the goal, then read on.


### Build and Deploy

1. Build the Docker container locally
```sh 
bash container_build.sh
```
2. Test the container locally
```shell
docker run -p 8080:8080 -it us-east1-docker.pkg.dev/gcloudsdk-on-wmm/gdocker/audiotranslatedemo:v20221121a
```
Then browse to http://localhost:8080/ to see the Streamlit application running locally.

4. Upload the container to Google Artifact Registry
```shell
UPLOAD=1 bash container_build.sh
```
5. Determine the DNS names of the frontend server for your deployment

6. Instantiate and configure the container in Google Cloud Run on the Google Cloud console.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To interact with the deployed demo system, browse to https://audio.nyctaxi.me/.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [X] Make the demo look nicer in streamlit
- [ ] The streamlit audio recorder does not seem to be stable on mobile devices. Investigate alternatives.

See the [open issues](https://github.com/willgroves/audiotranslateui/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

William Groves - [@willgrovesemail](https://twitter.com/willgrovesemail)

Project Link: [https://github.com/willgroves/audiotranslatedemo](https://github.com/willgroves/audiotranslatedemo)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## References
* Widget for recording audio in streamlit frontends: [here](https://github.com/Joooohan/audio-recorder-streamlit)
* Deploying to Google Cloud Platform App Engine seems well documented: [here](https://towardsdatascience.com/deploying-streamlit-apps-to-google-cloud-platform-2b8b1f9b94a9)
* A tutorial on deploying Streamlit applications to Google Cloud Run can be found [here](https://towardsdatascience.com/deploying-streamlit-apps-to-google-cloud-run-2f1d1a5b9527).
* [Another article](https://www.artefact.com/blog/how-to-deploy-and-secure-your-streamlit-app-on-gcp/)
* Name collisions for paths ending in the character z does seem to be a problem for GCP (e.g. /healthz, which is a core component of streamlit): [here](https://stackoverflow.com/questions/74185653/deploy-streamlit-on-gcp-cloud-run)
* A great template: [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

## Appendix

It is also possible to run the whisper model from the command line with examples like below:
```shell 
whisper src/audio.wav --language zh
whisper src/audio.wav --language zh --task translate
```

