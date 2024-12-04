# Audio Processing Scripts

This repository contains two Python scripts designed to handle audio transcription tasks. The scripts utilize the Whisper AI model for transcribing audio files into text format. Below is a detailed description of each script and their usage.

## Files

### 1. `convert-m4a.py`
#### Description
This script transcribes an `.m4a` audio file into text using the Whisper model. The transcription is saved to a text file.

#### Features
- Loads the Whisper AI model.
- Transcribes `.m4a` audio files.
- Outputs the transcription to `transcription.txt`.

#### Usage
1. Ensure you have the Whisper library installed:
   ```bash
   pip install whisper
   ```
2. Replace the placeholder path in the script with your `.m4a` file:
   ```python
   m4a_file = "input.m4a"  # Replace with your m4a file path
   ```
3. Run the script:
   ```bash
   python convert-m4a.py
   ```
4. The transcription will be saved to `transcription.txt`.

---

### 2. `convert-txt.py`
#### Description
This script extracts audio from a video file (e.g., `.mp4`) and transcribes it into text using the Whisper model. The transcription is saved to a text file.

#### Features
- Extracts audio from video files.
- Transcribes audio files into text.
- Saves the transcription to `transcription.txt`.

#### Usage
1. Ensure you have the required libraries installed:
   ```bash
   pip install moviepy whisper
   ```
2. Replace the placeholder paths in the script with your video and desired output paths:
   ```python
   video_file = "input.mp4"  # Replace with your MP4 file path
   audio_file = "output.wav"
   ```
3. Run the script:
   ```bash
   python convert-txt.py
   ```
4. The transcription will be saved to `transcription.txt`.

## Prerequisites
- Python 3.6 or later.
- Libraries:
  - `whisper`: AI model for transcription.
  - `moviepy`: For extracting audio from video (only required for `convert-txt.py`).

## Notes
- Ensure that the input file paths exist before running the scripts.
- The Whisper model may require substantial computational resources. Use smaller models (e.g., `base`) for faster transcription.

## License
This project is provided as-is under the MIT License. Use it freely with no warranty implied.

