import onnxruntime
import numpy as np
import tldextract
import os

# Load ONNX model from file
MODEL_PATH = os.path.join("models", "model.onnx")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"ONNX model not found at {MODEL_PATH}.\n"
        "Please download from:\n"
        "https://huggingface.co/pirocheto/phishing-url-detection/resolve/main/model.onnx"
    )

SESSION = onnxruntime.InferenceSession(MODEL_PATH)

def extract_features(url: str):
    ext = tldextract.extract(url)
    return [
        len(url),
        url.count("."),
        int(url.startswith("https")),
        int("login" in url.lower()),
        int("verify" in url.lower()),
        int("account" in url.lower())
    ]

def predict_phishing(url: str) -> str:
    feats = np.array([extract_features(url)], dtype=np.float32)
    inputs = {SESSION.get_inputs()[0].name: feats}
    outputs = SESSION.run(None, inputs)
    prob_phishing = outputs[1][0][1]
    return "Malicious" if prob_phishing > 0.5 else "Safe"
