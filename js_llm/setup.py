import os
import urllib.request
import ssl

# Disable SSL check to avoid certificate errors on some systems
ssl._create_default_https_context = ssl._create_unverified_context

# Configuration
BASE_DIR = os.getcwd()
WLLAMA_VERSION = "2.3.6"
FILES_TO_DOWNLOAD = [
    # (URL, Local Path)
    
    # 1. Tailwind CSS (UI)
    ("https://cdn.tailwindcss.com", "js/tailwindcss.js"),
    
    # 2. Wllama Main JS Library
    (f"https://cdn.jsdelivr.net/npm/@wllama/wllama@{WLLAMA_VERSION}/esm/index.js", "js/wllama/index.js"),
    
    # 3. Wllama WASM (Single Thread)
    (f"https://cdn.jsdelivr.net/npm/@wllama/wllama@{WLLAMA_VERSION}/src/single-thread/wllama.wasm", "js/wllama/single-thread/wllama.wasm"),
    
    # 4. Wllama WASM (Multi Thread)
    (f"https://cdn.jsdelivr.net/npm/@wllama/wllama@{WLLAMA_VERSION}/src/multi-thread/wllama.wasm", "js/wllama/multi-thread/wllama.wasm"),
    
    # 5. The AI Model (SmolLM2-360M)
    ("https://huggingface.co/professorf/SmolLM-135M-Instruct-gguf/resolve/main/SmolLM-135M-Instructt-q8_0.gguf?download=true","models/smollm2-135m-instryct-q8_0.gguf")
    # ("https://huggingface.co/ngxson/SmolLM2-360M-Instruct-Q8_0-GGUF/resolve/main/smollm2-360m-instruct-q8_0.gguf", "models/smollm2-360m-instruct-q8_0.gguf"),
]

def download_file(url, path):
    full_path = os.path.join(BASE_DIR, path)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    print(f"Downloading: {path}...")
    try:
        urllib.request.urlretrieve(url, full_path)
        print(" -> Done.")
    except Exception as e:
        print(f" -> ERROR: {e}")

def main():
    print("--- AI Robot Offline Setup ---")
    print(f"Installing to: {BASE_DIR}")
    
    for url, path in FILES_TO_DOWNLOAD:
        if os.path.exists(path):
            print(f"Skipping {path} (already exists)")
        else:
            download_file(url, path)
            
    print("\n--- Setup Complete! ---")
    print("To run the app, you MUST use a local server due to browser security.")
    print("Run this command in your terminal:")
    print("   python -m http.server 8000")
    print("Then open: http://localhost:8000")

if __name__ == "__main__":
    main()