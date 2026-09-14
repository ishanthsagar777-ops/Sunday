from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Sunday Core Operating System")

class SundayInput(BaseModel):
    prompt: str

class EnvironmentScan(BaseModel):
    target: str
    scan_type: str

@app.post("/api/sunday/interact")
async def sunday_interact(data: SundayInput):
    user_prompt = data.prompt.lower()
    
    if "status" in user_prompt or "systems" in user_prompt:
        reply = "All core systems are nominal, Ishanth. Ready for deployment."
    elif "scan" in user_prompt:
        reply = "Environment scanning protocols are standing by. Provide target details."
    else:
        reply = f"Command received and logged: '{data.prompt}'. Executing parameters."
        
    return {
        "status": "active",
        "sender": "Sunday",
        "response": reply
    }

@app.post("/api/sunday/scan")
async def sunday_scan(data: EnvironmentScan):
    return {
        "status": "completed",
        "target": data.target,
        "environment": data.scan_type,
        "results": "Scan sequence finalized. Environment secure."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
