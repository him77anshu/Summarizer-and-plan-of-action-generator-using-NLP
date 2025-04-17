import os
import assemblyai as aai
import moviepy.editor as mp
from dotenv import load_dotenv
    
load_dotenv() 
aai.settings.api_key= os.getenv("ASSEMBLY_API_KEY")

def transcribe_video(video_path):
    try:
        # Extracting audio from the video
        video = mp.VideoFileClip(video_path)
        audio_path = "temp_audio.wav"  
        video.audio.write_audiofile(audio_path)

        # Transcription of the audio that is extract from video
        with open(audio_path, "rb") as audio_file:
          
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(audio_file)
            

        os.remove(audio_path)

       
        with open("transcription.txt", "w") as o_f:
            o_f.write(transcript.text)  

        return transcript.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

video_path = "C:\\Users\\91950\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\video\\videoplayback.mp4"  
transcribed_text = transcribe_video(video_path)

if transcribed_text:
    print("Transcribed text:")
    print(transcribed_text)