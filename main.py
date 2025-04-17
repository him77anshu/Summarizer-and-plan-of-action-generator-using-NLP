import openai
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from summarizerM import summarize_text
import moviepy.editor as mp
from Email_send import send_mail
import assemblyai as aai
from dotenv import load_dotenv

load_dotenv() 
aai.settings.api_key = os.getenv("ASSEMBLY_API_KEY")
# openai.api_key = os.getenv("OPENAI_API_KEY")

# New transcribe_video function
def transcribe_video(video_path):
    try:
        # Extract audio from video
        video = mp.VideoFileClip(video_path)
        audio_path = "temp_audio.wav"
        video.audio.write_audiofile(audio_path)

        # Transcription of the extracted audio
        with open(audio_path, "rb") as audio_file:
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(audio_file)
            
        os.remove(audio_path)  # Clean up temporary audio file

        # Save transcription to file
        with open("transcription.txt", "w") as o_f:
            o_f.write(transcript.text)

        return transcript.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error transcribing video: {e}"

# Function to select video file
def select_file():
    video_path.set(filedialog.askopenfilename(filetypes=[("Video/Audio files", "*.mp4;*.avi;*.mov;*.wav")]))
    messagebox.showinfo("File Selected", f"Selected file: {video_path.get()}")

# Function to transcribe selected file (using the new transcribe_video function)
def transcribe_selected_file():
    if video_path.get():
        transcription_result = transcribe_video(video_path.get())
        transcription.set(transcription_result)
        if "Error" in transcription_result:
            messagebox.showerror("Error", transcription_result)
        else:
            messagebox.showinfo("Transcription Complete", "Audio transcription completed successfully.")
    else:
        messagebox.showwarning("No File Selected", "Please select a video or audio file first.")


# Function to Summarizer and Plan of action genrator
def summarize_and_generate_plan():
    text = transcription.get()
    if text:
        try:
            # Summarize the transcription text
            summary = summarize_text(text)
            summary_text.delete(1.0, tk.END)  # Clear the summary widget
            summary_text.insert(tk.END, summary)

            
            prompt = (
                f"Based on the following meeting transcript, create a detailed plan of action with **exactly 5 points**:\n\n"
                f"Meeting Transcript:\n{text}\n\n"
                f"Plan of Action:\n"
            )

            # Call the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600,
                n=1,
                stop=None,
                temperature=0.7,
            )

            # Extract the response and limit to 5 points
            plan_of_action = response.choices[0].message['content'].strip()

            # Insert the Plan of Action into the text widget
            action_plan_text.delete(1.0, tk.END)  
            action_plan_text.insert(tk.END, plan_of_action)

            # Notify the user that the process is complete
            messagebox.showinfo("Summarization and Plan Generation Complete", "Summary and Plan of Action generated successfully.")

        except Exception as e:
            # Handle errors during summarization or plan generation
            messagebox.showerror("Error", f"An error occurred during summarization or plan generation: {e}")
    else:
        # Warn the user if no transcription is available
        messagebox.showwarning("No Transcription", "Please transcribe audio before summarizing and generating a Plan of Action.")

# Function to send the email
def send_email():
    recipient = recipient_entry.get()
    summary = summary_text.get("1.0", tk.END).strip()
    plan = action_plan_text.get("1.0", tk.END).strip()
    if recipient and summary and plan:
        try:
            send_mail([recipient], summary, plan)
            messagebox.showinfo("Email Sent", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
    else:
        messagebox.showwarning("Missing Information", "Please ensure all fields are filled.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Meeting Summarization and Plan of Action")
root.geometry("600x800")

video_path = tk.StringVar()
transcription = tk.StringVar()

# Video file selection
tk.Label(root, text="Select Video/Audio File").pack(pady=5)
tk.Entry(root, textvariable=video_path, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=select_file).pack(pady=5)
tk.Button(root, text="Transcribe Selected File", command=transcribe_selected_file).pack(pady=10)

# Transcription display
tk.Label(root, text="Transcription").pack(pady=5)
tk.Entry(root, textvariable=transcription, width=70).pack(pady=5)

# Summarize and Generate Plan of Action Button
tk.Button(root, text="Summarize Text & Plan Generate", command=summarize_and_generate_plan).pack(pady=10)

# Summary display with increased height
tk.Label(root, text="Summary").pack(pady=5)
summary_text = tk.Text(root, width=70, height=10, wrap=tk.WORD)
summary_text.pack(pady=5)

# Plan of Action display with increased height
tk.Label(root, text="Plan of Action").pack(pady=5)
action_plan_text = tk.Text(root, width=70, height=10, wrap=tk.WORD)
action_plan_text.pack(pady=5)

# Recipient Email
tk.Label(root, text="Recipient Email").pack(pady=5)
recipient_entry = tk.Entry(root, width=50)
recipient_entry.pack(pady=5)

# Send Email Button
tk.Button(root, text="Send Email", command=send_email).pack(pady=20)

root.mainloop()

