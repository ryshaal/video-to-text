
# Video to Text Transcription Project

This project is designed to convert video files into text by extracting the audio from the video and transcribing it using Python's `speech_recognition` library. The transcribed text files are saved in a dedicated folder.

## Features

- Extract audio from video files.
- Convert the extracted audio to text using Google Web Speech API.
- Handle different video formats.

## Requirements

Before running the project, ensure you have installed the following:

- Python 3.x
- `ffmpeg` for extracting audio from video.
- `speechrecognition` library for transcribing audio to text.

## Setup and Installation

### 1. Clone the repository

Clone this repository to your local machine:
```bash
git clone https://github.com/ryshaal/video-to-text.git
cd video-to-text
```

### 2. Install Required Libraries

Install the necessary Python packages:
```bash
pip install -r requirements.txt
```

Make sure `ffmpeg` is installed:
- For Linux:
  ```bash
  sudo apt install ffmpeg
  ```
- For Windows, download `ffmpeg` from [here](https://ffmpeg.org/download.html) and follow the installation instructions.

### 3. Place Videos in Input Folder

Place the video files you want to transcribe into the `video_input/` folder.

### 4. Run the Script

Run the script to process the videos:
```bash
python main.py
```

### 5. Output

The transcribed text files will be saved in the `transcribe/` folder with the same name as the video file.

---

## Running on Termux (Android)

You can also run this project on Android using Termux. Follow these steps:

### Install Prerequisites on Termux

1. Update Termux and install essential packages:
   ```bash
   pkg update && pkg upgrade
   pkg install python ffmpeg
   ```

2. Install `pip` and required Python libraries:
   ```bash
   pkg install python-pip
   pip install speechrecognition
   ```

3. Install `ffmpeg` to handle video-to-audio conversion:
   ```bash
   pkg install ffmpeg
   ```

### Running the Script on Termux

1. Clone the repository in Termux:
   ```bash
   git clone https://github.com/ryshaal/video-to-text.git
   cd video-to-text
   ```

2. Place your video files in the `video_input/` folder:
   You can use the Termux storage to access your Android files by running the following command:
   ```bash
   termux-setup-storage
   ```

   Then, copy your video files into the `video_input/` folder using Termux:
   ```bash
   cp /sdcard/Download/example.mp4 ./video_input/
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. Follow the instructions, and the transcribed text files will be saved in the `transcribe/` folder.

### Notes for Termux

- Ensure that Termux has access to your storage. If needed, you can copy files from your internal storage to Termux using the command `cp` as shown above.
- The performance on Android might be slower than on a desktop environment, so be patient while the video conversion and transcription process runs.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
