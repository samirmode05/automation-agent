import subprocess
import os
from fastapi import HTTPException

def run_datagen(email: str):
    try:
        # Define the command to run datagen.py with the email argument
        script_path = os.path.join(os.getcwd(), "datagen.py")
        result = subprocess.run(
            ["python", script_path, email], 
            check=True, capture_output=True, text=True
        )
        
        return {"output": result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error running datagen: {e.stderr}")

def handle_task(task: str):
    if not isinstance(task, str) or not task:
        raise HTTPException(status_code=400, detail="Invalid task format.")
    
    # Check if the task is for A1
    if "Run datagen with" in task:
        # Extract email from task
        import re
        match = re.search(r'Run datagen with "([^"]+)"', task)
        if match:
            email = match.group(1)
            return run_datagen(email)
        else:
            raise HTTPException(status_code=400, detail="Email not found in task.")
    
    raise HTTPException(status_code=400, detail="Unsupported task.")

def execute_task(task_description):
    print(f"Received task: {task_description}")  # Debugging line

    if "wednesday" in task_description.lower() or "count" in task_description.lower():
        try:
            subprocess.run(["python", "tasks/count_wednesdays.py"], check=True)
            return {"status": "success", "message": "Wednesdays counted successfully."}, 200
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": f"Failed to execute task: {str(e)}"}, 500
    else:
        return {"status": "error", "message": "Unknown task."}, 400
