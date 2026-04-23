
import pandas as pd

def extract_features(packet_data):
    features = {
        'packet_size': len(packet_data),
        'protocol': packet_data.get('protocol', 0)
    }
    return pd.DataFrame([features])
