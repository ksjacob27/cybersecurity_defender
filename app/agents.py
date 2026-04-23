from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
print("[DEBUG] Loaded OpenAI key:", os.getenv("OPENAI_API_KEY"))
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def traffic_classifier_agent(data):
    features = f"Packet Size: {data['packet_size']}, Protocol: {data['protocol']}"
    prompt = f"Given the following network traffic features: {features}. Is this traffic benign or malicious?"
    return call_openai(prompt)

def threat_analyzer_agent(data):
    features = f"Packet Size: {data['packet_size']}, Protocol: {data['protocol']}"
    prompt = f"Given this malicious traffic: {features}. What is the most likely threat type and how severe is it?"
    return call_openai(prompt)

def response_planner_agent(threat_type):
    prompt = f"Given the detected threat: {threat_type}. What immediate action should be taken to mitigate it?"
    return call_openai(prompt)

def logger_agent(summary):
    print("[LOGGER AGENT] Event Summary:", summary)

def call_openai(prompt):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a cybersecurity analyst agent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
