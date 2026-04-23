# Autonomous Cybersecurity Defender (ThunderClient-Ready Version)

## Dataset link -
- https://www.unb.ca/cic/datasets/ids-2017.html

## Features
- Uses OpenAI GPT-4o agents to classify and respond to threats.
- Integrated with Thunder Client for easy testing in VS Code.
- REST API powered by FastAPI.

## How to Use
1. Install dependencies:
   pip install -r requirements.txt

2. Run the API server:
   uvicorn app.api:app --host 0.0.0.0 --port 8000

3. Use Thunder Client (in VS Code) to send a POST request to:
   http://localhost:8000/predict

Body (JSON):
{
  "packet_size": 500,
  "protocol": 2
}
