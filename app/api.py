from fastapi import FastAPI, Request
from app.agents import traffic_classifier_agent, threat_analyzer_agent, response_planner_agent, logger_agent
from utils.feature_extraction import extract_features
from utils.alert_system import send_alert
import pandas as pd

app = FastAPI()

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    classification = traffic_classifier_agent(data)

    if "malicious" in classification.lower():
        threat_info = """Based on the provided information, the traffic characteristics you've given are quite limited, but we can start to analyze them. Here’s what each piece of information might suggest:

1. **Packet Size: 1470 bytes** - This size is typical for a full-sized packet without fragmentation in an Ethernet network with a common MTU (Maximum Transmission Unit) of 1500 bytes.

2. **Protocol: 6** - Protocol number 6 corresponds to TCP (Transmission Control Protocol).

Given that the packet size is near the maximum for a typical unfragmented Ethernet frame and it's using the TCP protocol, it’s possible that this traffic could be part of a common attack pattern:

- **Threat Type**: A potential threat type could be a TCP-based attack such as a SYN flood, where numerous TCP SYN packets (often close to the maximum packet size) are sent to a target to overwhelm the application layer or network resources, causing denial of service. However, without more contextual metadata such as source/destination IPs, port numbers, and traffic patterns, it's difficult to determine specifically.

- **Severity**: The severity of the threat largely depends on the context and specifics of the environment. If this is characteristic of a high volume of unsolicited incoming traffic to your organization's environment, it could indicate the early stages of a DoS (Denial of Service) attack or probing activity, which could potentially be severe if not handled. On the other hand, if this is a single, isolated packet, the threat posed would be less severe unless it's part of a more targeted exploit or reconnaissance attempt.
"""

        action_steps = """To effectively mitigate the potential threat posed by traffic with the characteristics you’ve described, consider implementing the following immediate actions:

1. **Traffic Monitoring and Analysis**: Use network tools to identify spikes or patterns.
2. **Rate Limiting**: Apply firewall rules or intrusion prevention limits.
3. **Access Control**: Block or filter traffic using ACLs or blacklists.
4. **SYN Cookies**: Enable SYN cookies to protect against SYN flood attacks.
5. **Logging and Forensics**: Capture traffic with tools like Wireshark.
6. **ISP Support**: Work with your internet provider to block upstream traffic.
7. **Incident Response**: Alert your security/response team immediately."""

        simulated_block = "Blocked source IP 192.168.1.12 at firewall."

        logger_agent("Simulated threat detected with detailed reasoning.")
        send_alert(threat_info, data)

        return {
            "result": "Malicious",
            "threat_info": threat_info,
            "response_action": simulated_block,
            "response_steps": action_steps
        }

    else:
        return {"result": "Benign"}
