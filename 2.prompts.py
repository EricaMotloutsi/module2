import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError ("Open api key not found frin env file")

def get_response(prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=400,
        messages= [{"role":"user", "content":prompt}]
    )
    return response.choices[0].message.content

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

response = get_response(prompt)
print(response)

finance_text="""
Finance is the study of money and how it is used. Specifically, it deals with the questions of how an individual, company or government acquires the money needed and how they then spend or invest that money. Core financial theories can largely be divided into the following categories: financial economics, mathematical finance and valuation. In the context of institutions, finance is often split into the following major categories: investment management, corporate finance, personal finance and public finance.
"""

prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

response = get_response(prompt)
print(response)

