from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import requests
import json

def test_model_loading():
    print("Testing Phi-3 Mini model loading...")
    try:
        model = AutoModelForCausalLM.from_pretrained("microsoft/phi-3-mini-4k-instruct")
        tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-4k-instruct")
        print("✓ Model loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Error loading model: {str(e)}")
        return False

def test_api_endpoints():
    print("\nTesting API endpoints...")
    base_url = "http://localhost:8000"
    endpoints = [
        ("Health Check", "GET", "/health", None),
        ("Business Ideas", "POST", "/generate", {"prompt": "Suggest a business idea", "parameters": {"max_length": 100}}),
        ("Market Research", "POST", "/market-research", {"prompt": "Analyze coffee shop market", "parameters": {"max_length": 100}}),
        ("Legal Advice", "POST", "/legal-advice", {"prompt": "What licenses do I need?", "parameters": {"max_length": 100}})
    ]

    for name, method, endpoint, data in endpoints:
        try:
            if method == "GET":
                response = requests.get(f"{base_url}{endpoint}")
            else:
                response = requests.post(f"{base_url}{endpoint}", json=data)
            
            if response.status_code == 200:
                print(f"✓ {name}: Success")
                print(f"  Response: {json.dumps(response.json(), indent=2)[:150]}...")
            else:
                print(f"✗ {name}: Failed with status {response.status_code}")
        except Exception as e:
            print(f"✗ {name}: Error - {str(e)}")

if __name__ == "__main__":
    print("=== AI Model System Test ===\n")
    
    if test_model_loading():
        test_api_endpoints()
    else:
        print("\nSkipping API tests due to model loading failure")