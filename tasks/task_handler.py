import subprocess
from fastapi import HTTPException

def handle_task(task: str):
    if "install uv" in task and "run" in task:
        return install_and_run_uv(task)
    elif "format" in task and "prettier" in task:
        return format_markdown_with_prettier(task)
    else:
        raise HTTPException(status_code=400, detail="Task not recognized or not supported yet")

def format_markdown_with_prettier(task: str):
    file_path = "/data/format.md"

    
    try:
        with open(file_path, "r") as file:
            pass
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

    # Run Prettier
    try:
        subprocess.run(["prettier", "--write", file_path], check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Prettier formatting failed: {str(e)}")
    
    return {"status": "Success", "message": f"{file_path} formatted with Prettier 3.4.2"}
