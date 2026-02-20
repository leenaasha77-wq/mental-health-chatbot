# Step 1:setup FastAPI backend
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn



app = FastAPI()
 

# Step 2:receive and validate request from frontend
class Query(BaseModel):
    message: str


@app.post("/ask")
async def ask(qurey: Query):
    # AI agent 
    response = "This is from backend v2"

# Step 3:send response to the frontend
    return {"response": response} 
 
if __name__ == "__main__":
    uvicorn.run("main:app",host= "127.0.0.1", port=8000, reload=True)