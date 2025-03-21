from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import socket
from typing import Dict, Any
from transformers import AutoModelForCausalLM, AutoTokenizer

# Add the ModelResponse class definition
class ModelResponse(BaseModel):
    generated_text: str
    model_used: str
    status: str

class Prompt(BaseModel):
    prompt: str
    parameters: Dict[str, Any] = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def find_available_port(start_port=8000, max_port=8100):
    for port in range(start_port, max_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                return port
        except OSError:
            continue
    raise OSError("No available ports found")

@app.get("/")
async def root():
    return {
        "message": "AI Assistant API Server",
        "version": "1.0.0",
        "endpoints": [
            "/health",
            "/generate",
            "/market-research",
            "/legal-advice"
        ],
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "models": ["gpt2", "distilbert-base-cased", "huggingface-summarizer"],
        "server_version": "1.0.0"
    }

# Initialize Phi-3 Mini model
phi_model = AutoModelForCausalLM.from_pretrained("microsoft/phi-3-mini-4k-instruct")
phi_tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-4k-instruct")

async def generate_phi_response(prompt: str, context: str) -> str:
    full_prompt = f"{context}\n{prompt}"
    inputs = phi_tokenizer(full_prompt, return_tensors="pt")
    outputs = phi_model.generate(**inputs, max_length=500)
    return phi_tokenizer.decode(outputs[0])

@app.post("/generate", response_model=ModelResponse)
async def generate(prompt: Prompt):
    try:
        context = "Act as a business idea generator. Suggest detailed and innovative business ideas based on the following request:"
        response = await generate_phi_response(prompt.prompt, context)
        return {
            "generated_text": response,
            "model_used": "phi-3-mini",
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/market-research", response_model=ModelResponse)
async def market_research(prompt: Prompt):
    try:
        context = "Act as a market research analyst. Provide detailed market analysis and competitor insights for the following query:"
        response = await generate_phi_response(prompt.prompt, context)
        return {
            "generated_text": response,
            "model_used": "phi-3-mini",
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/legal-advice", response_model=ModelResponse)
async def legal_advice(prompt: Prompt):
    try:
        context = "Act as a legal advisor. Provide business-related legal guidance and regulatory information for the following question:"
        response = await generate_phi_response(prompt.prompt, context)
        return {
            "generated_text": response,
            "model_used": "phi-3-mini",
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    try:
        port = find_available_port()
        print(f"\nStarting server on port {port}")
        uvicorn.run(app, host="0.0.0.0", port=port)
    except Exception as e:
        print(f"Error starting server: {e}")