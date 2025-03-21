import requests
import json
import sys
from time import sleep

def find_server_port(start_port=8000, max_port=8100):
    for port in range(start_port, max_port):
        try:
            response = requests.get(f"http://localhost:{port}/health", timeout=1)
            if response.ok:
                return port
        except requests.exceptions.RequestException:
            continue
    return None

def test_endpoints():
    port = find_server_port()
    if not port:
        print("\nError: Cannot find running server!")
        print("Please start the server first by running:")
        print("python server.py")
        return
    
    base_url = f"http://localhost:{port}"
    
    def test_health():
        try:
            response = requests.get(f"{base_url}/health")
            print("\nHealth Check:")
            print(json.dumps(response.json(), indent=2))
        except requests.exceptions.RequestException as e:
            print(f"\nHealth Check Error: {str(e)}")
        
    def test_model(endpoint, prompt):
        print(f"\nTesting {endpoint}:")
        try:
            response = requests.post(
                f"{base_url}/{endpoint}",
                json={"prompt": prompt, "parameters": {"max_length": 100}},
                timeout=10
            )
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=2))
            else:
                print(f"Error: Server returned status code {response.status_code}")
                print("Response:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
    
    # Run tests
    test_health()
    test_model("generate", "Create a mobile app for pet owners")
    test_model("market-research", "Analyze the pet care industry")
    test_model("legal-advice", "What licenses do I need for a pet care business?")

if __name__ == "__main__":
    test_endpoints()