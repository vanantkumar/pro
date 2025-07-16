import streamlit as st
from openai import OpenAI, NotFoundError, RateLimitError

client = OpenAI()

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant tasked with generating professional email replies.

Tone: {tone}

Email:
{email_text}

Reply:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
    except NotFoundError:
        # Fallback to GPT-3.5-turbo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
    except RateLimitError:
        return "⚠️ You have exceeded your OpenAI usage quota. Please check your billing details."

    return response.choices[0].message.content







