# Video Language Conversion Tool

A Python tool to convert videos from one language to another by extracting audio, transcribing it, translating the text, and adding subtitles to the video.

## Features
- Extracts audio from video files using `ffmpeg`.
- Converts speech to text using `SpeechRecognition`.
- Translates text into multiple languages using `Googletrans`.
- Adds translated subtitles to the video using `ffmpeg`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hemantchilkuri/video-language-converter.git

## Navigate to the project directory:
cd video-language-converterInstall dependencies:

## install dependencies:
pip install pydub SpeechRecognition googletrans==4.0.0-rc1

## Install ffmpeg (required for audio extraction and subtitle addition):

1. On Ubuntu:
sudo apt install ffmpeg

2. On macOS (using Homebrew):
brew install ffmpeg

## Usage
1. Place your video file in the project directory (e.g., input_video.mp4).
2. Run the script:
   python video_converter.py
3. Follow the prompts to select the target language.
4. The output video with translated subtitles will be saved as output_video.mp4

## Technologies Used
Python
FFmpeg (for audio extraction and subtitle addition)
SpeechRecognition (for speech-to-text)
Googletrans (for translation)

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Supported Languages
English (en)
Spanish (es)
French (fr)
German (de)
