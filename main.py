from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    # Placeholder for task execution logic
    return {"status": "Task received", "task": task}

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return PlainTextResponse(content, media_type="text/plain")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
