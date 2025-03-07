import os
import subprocess
from googletrans import Translator
from pydub import AudioSegment
import speech_recognition as sr

def extract_audio(video_path, audio_path):
    """Extract audio from a video file using ffmpeg."""
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path} -y"
    subprocess.call(command, shell=True)

def transcribe_audio(audio_path):
    """Convert speech in an audio file to text using SpeechRecognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from the speech recognition service; {e}"

def translate_text(text, dest_language):
    """Translate text to the target language using Googletrans."""
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def add_subtitles_to_video(video_path, output_path, subtitles):
    """Add subtitles to a video using ffmpeg."""
    subtitle_file = "subtitles.srt"
    with open(subtitle_file, "w") as f:
        f.write(f"1\n00:00:00,000 --> 00:10:00,000\n{subtitles}")
    command = f"ffmpeg -i {video_path} -vf subtitles={subtitle_file} {output_path} -y"
    subprocess.call(command, shell=True)
    os.remove(subtitle_file)

def convert_video_language(video_path, output_path, dest_language):
    """Convert a video's language by extracting audio, transcribing, translating, and adding subtitles."""
    audio_path = "temp_audio.wav"
    
    # Step 1: Extract audio from the video
    extract_audio(video_path, audio_path)
    
    # Step 2: Transcribe the audio to text
    text = transcribe_audio(audio_path)
    print(f"Transcribed Text: {text}")
    
    # Step 3: Translate the text to the target language
    translated_text = translate_text(text, dest_language)
    print(f"Translated Text: {translated_text}")
    
    # Step 4: Add subtitles to the video
    add_subtitles_to_video(video_path, output_path, translated_text)
    
    # Clean up temporary files
    os.remove(audio_path)

if __name__ == "__main__":
    video_path = "input_video.mp4"  # Replace with your input video file
    output_path = "output_video.mp4"  # Replace with your desired output file
    dest_language = "es"  # Replace with the target language code (e.g., "es" for Spanish)
    
    convert_video_language(video_path, output_path, dest_language)
