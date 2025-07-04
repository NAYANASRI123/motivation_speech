#  Daily Motivation Generator

A simple web app that generates motivational quotes based on your mood using **OpenAI GPT-3.5** and **Gradio**.

---

## Features

- Powered by OpenAI GPT (via API)
- Choose from moods like:
  - Feeling Anxious
  - Need Focus
  - Feeling Low
  - Want to Achieve Goals
  - Need Confidence
- Clean and simple Gradio interface
- API key securely managed via Hugging Face Secrets

---

## Live Demo

Try it now on Hugging Face Spaces:  
 [Click here to open the app](https://huggingface.co/spaces/Nayanhf/motivation_speech)

---
## Screenshot
![App Screenshot](screenshot.png)

---
## 🛠 How It Works

1. User selects a mood
2. App sends a prompt to GPT-3.5 using OpenAI API
3. GPT responds with a motivational quote
4. Quote is shown on screen via Gradio UI

---

## Files

| File              | Purpose                              |
|-------------------|--------------------------------------|
| `app.py`          | Main Python app (Gradio + GPT)       |
| `requirements.txt`| Python dependencies                  |
| `README.md`       | Project description (this file)      |

---

## 🧪 Run It Locally

```bash
pip install -r requirements.txt
python app.py
