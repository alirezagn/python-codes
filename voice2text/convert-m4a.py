import whisper

def transcribe_audio(m4a_file):
    """
    Transcribe the m4a audio file to text using Whisper.
    """
    try:
        # Load the Whisper model
        model = whisper.load_model("base")  # You can use "small", "medium", "large" for better accuracy
        
        # Transcribe the m4a audio file directly
        result = model.transcribe(m4a_file)
        print(f"Transcription: {result['text']}")
        return result['text']
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

if __name__ == "__main__":
    # Path to your input m4a file
    m4a_file = "input.m4a"  # Replace with your m4a file path

    # Transcribe the m4a file to text
    transcribed_text = transcribe_audio(m4a_file)
    
    # Save the transcription to a text file
    if transcribed_text:
        with open("transcription.txt", "w") as f:
            f.write(transcribed_text)
        print("Transcription saved to transcription.txt")