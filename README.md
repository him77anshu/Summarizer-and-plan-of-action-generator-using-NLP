# 🧠 Meeting Summarizer & Plan of Action Generator using NLP

This project is a powerful NLP-based tool designed to streamline post-meeting workflows by automatically generating concise summaries and actionable plans from recorded meetings. With an intuitive Tkinter GUI, it allows users to upload meeting videos, transcribe them, generate summaries and plans, and email the results — all in one seamless flow.

---

## 🚀 Features

- 🎙️ **Audio-to-Text Transcription** using OpenAI’s Whisper model  
- 📝 **Automatic Summary Generation** via Hugging Face Transformers  
- ✅ **Plan of Action Creation** powered by GPT-4 Turbo  
- 📧 **Email Integration** for easy sharing of results  
- 🖥️ **User-Friendly GUI** built with Tkinter  
- ⚙️ **Video-to-Audio Conversion** using FFmpeg  
- 🔄 **Fully Automated Workflow** from input to output  

---

## 📌 Project Scope

### ✅ Included
- Video-to-audio conversion  
- Audio transcription  
- Summary and action point generation  
- Email delivery of results  
- Real-time progress updates in the GUI  

### ❌ Excluded
- Real-time (live) meeting processing  
- Fine-tuning of models for domain-specific jargon  

---

## 🧱 Tech Stack

- **Language**: Python  
- **GUI**: Tkinter  
- **Audio/Video**: FFmpeg  
- **Transcription**: OpenAI Whisper  
- **Summarization**: Hugging Face Transformers  
- **Action Generation**: GPT-4 Turbo (via OpenAI API)  
- **Emailing**: smtplib  
- **Others**: os, re, subprocess  

---

## 📂 Architecture

- **Input Module** – Handles file upload and conversion  
- **Processing Module** – Transcribes, summarizes, and generates action points  
- **Email Module** – Sends outputs via email  
- **GUI Module** – Manages user interactions  

---

## 🛠️ Setup Instructions

### Clone the Repository
```bash
https://github.com/him77anshu/Summarizer-and-plan-of-action-generator-using-NLP.git
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up API Keys
Add your OpenAI API key in the appropriate environment or config file.

### Run the App
```bash
python main.py
```

---

## ⚙️ Requirements

### Functional
- Upload and convert video to audio  
- Transcribe audio using Whisper  
- Summarize using Transformers  
- Generate action points with GPT-4  
- Email the outputs  

### Non-Functional
- Fast processing (<5 min transcription for 10 min audio with GPU)  
- GUI responsiveness  
- Accuracy ≥ 90% for clear audio  
- Robust email delivery  

---

## 📸 Screenshots

*(Add screenshots of your Tkinter GUI here)*

---

## 🚧 Limitations

- Accuracy may drop with poor-quality or noisy audio  
- Real-time/live meeting support is not available  
- Relies on third-party APIs; may incur cost or rate limits  

---

## 🧪 Development Approach

The project followed an iterative approach:

1. File upload and conversion  
2. Audio transcription  
3. Summary generation  
4. Action point generation  
5. Email module  
6. GUI integration and testing  
