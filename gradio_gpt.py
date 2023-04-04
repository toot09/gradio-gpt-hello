import gradio as gr
import requests
import os
import openai
from gradio import components

openai.api_key = "openai api-key"

def call_gpt_api(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello!"}
            ]
        )
        print(completion.choices[0].message)
        return completion.choices[0].message.content
    
    except Exception as e:
        return "Error: API call failed"


input_text = components.Textbox(lines=5, label="Input prompt")
output_text = components.Textbox(label="GPT-generated text")
interface = gr.Interface(fn=call_gpt_api, inputs=input_text, outputs=output_text)

app = interface.launch()
print("App is running on port:", app.port)
