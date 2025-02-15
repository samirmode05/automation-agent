from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from tasks.task_handler import handle_task

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    try:
        result = handle_task(task)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return PlainTextResponse(content, media_type="text/plain")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
