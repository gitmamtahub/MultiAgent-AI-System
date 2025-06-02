import json

def detect_format(input_data):
    if isinstance(input_data, dict):
        return "JSON"
    elif isinstance(input_data, str):
        if input_data.strip().startswith("{") or input_data.strip().startswith("["):
            try:
                json.loads(input_data)
                return "JSON"
            except:
                pass
        if "From:" in input_data and "Subject:" in input_data:
            return "Email"
        return "PlainText-PDF"
    return "Unknown"

