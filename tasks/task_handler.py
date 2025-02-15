import subprocess
from fastapi import HTTPException

def handle_task(task: str):
    # Example task: "Format /data/format.md using prettier@3.4.2"
    parts = task.split(" ")
    if len(parts) < 5:
        raise HTTPException(status_code=400, detail="Invalid task format.")
    
    action = parts[0]  # Format
    file_path = parts[1]  # /data/format.md
    tool = parts[3]  # prettier
    version = parts[4]  # 3.4.2
    
    if action.lower() == "format" and tool.lower() == "prettier":
        # Construct the command to run
        command = ["npx", f"prettier@{version}", "--write", file_path]
        
        try:
            # Run the command and capture the output
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {"status": "success", "output": result.stdout}
        
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.stderr}
    
    else:
        raise HTTPException(status_code=400, detail="Unsupported task.")
