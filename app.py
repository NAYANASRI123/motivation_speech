import os
import gradio as gr
from openai import OpenAI


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt_map = {
    "Feeling Anxious": "Give me a calming motivational quote to ease anxiety.",
    "Need Focus": "Give me a motivational quote to improve focus and concentration.",
    "Feeling Low": "Give me a positive quote to uplift my spirits.",
    "Want to Achieve Goals": "Give me a motivational quote to inspire goal-setting and success.",
    "Need Confidence": "Give me a powerful quote to boost self-confidence."
}


def generate_quote(mood):
    prompt = prompt_map.get(mood, "Give me a motivational quote.")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=60
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"

gr.Interface(
    fn=generate_quote,
    inputs=gr.Dropdown(
        choices=list(prompt_map.keys()),
        label="Your current mood"
    ),
    outputs=gr.Textbox(label="Motivational Quote"),
    title="🌟 Daily Motivation Generator",
    description="Select how you're feeling and get a personalized motivational quote powered by GPT-3.5/4."
).launch()
