# Video to Text Converter

This Python project allows you to convert video files into audio (WAV) format and transcribe the audio into text using Google Speech Recognition. The program supports multiple languages and automatically processes files in the specified input folder.

## Features
- Convert video files (.mp4, .avi, .mov, .mkv) to WAV format using `ffmpeg`.
- Transcribe audio files using Google Speech Recognition API (`SpeechRecognition` library).
- Supports multiple languages, including Indonesian (`id-ID`), English (`en-US`), and Spanish (`es-ES`).
- Automatically deletes the audio files after successful transcription.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ryshaal/video-to-text.git
