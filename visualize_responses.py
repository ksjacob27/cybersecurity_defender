import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_folder = "data"
response_folder = "responses"
combined = []

# Loop through 5 inputs and their corresponding responses
for i in range(1, 6):
    input_file = f"sample_input_{i}.json"
    response_file = f"sample_input_{i}_response.json"

    with open(os.path.join(input_folder, input_file)) as f_in:
        input_data = json.load(f_in)

    with open(os.path.join(response_folder, response_file)) as f_out:
        response_data = json.load(f_out)

    combined.append({
        "sample": f"Input {i}",
        "packet_size": input_data.get("packet_size"),
        "protocol": input_data.get("protocol"),
        "result": response_data.get("result", "Unknown")
    })

df = pd.DataFrame(combined)

# ✅ Plot 1: Prediction Result Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="result", palette="Set2")
plt.title("Prediction Result Distribution")
plt.xlabel("Prediction Result")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("prediction_distribution.png")
plt.show()

# ✅ Plot 2: Packet Size per Input by Result
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x="sample", y="packet_size", hue="result", palette="pastel")
plt.title("Packet Size per Input by Result")
plt.ylabel("Packet Size")
plt.xlabel("Sample Input")
plt.tight_layout()
plt.savefig("packet_size_vs_result.png")
plt.show()

# ✅ Plot 3: Protocol vs Prediction Result
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="protocol", hue="result", palette="muted")
plt.title("Protocol vs Prediction Result")
plt.xlabel("Protocol Number")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("protocol_vs_result.png")
plt.show()
