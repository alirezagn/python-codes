import os
from moviepy.editor import VideoFileClip
import whisper

def extract_audio_from_video(video_path, audio_path):
    """Extracts audio from an MP4 file."""
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        print(f"Audio extracted to {audio_path}")
    except Exception as e:
        print(f"Error extracting audio: {e}")

def transcribe_audio_to_text(audio_path, model_name="base"):
    """Transcribes audio to text using Whisper."""
    try:
        model = whisper.load_model(model_name)
        result = model.transcribe(audio_path)
        return result['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

if __name__ == "__main__":
    # Paths
    video_file = "input.m4a"  # Replace with your MP4 file path
    audio_file = "output.wav"
    output_text_file = "transcription.txt"

    # Extract audio
    extract_audio_from_video(video_file, audio_file)

    # Transcribe audio
    transcription = transcribe_audio_to_text(audio_file)
    if transcription:
        with open(output_text_file, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"Transcription saved to {output_text_file}")
    else:
        print("Transcription failed.")
