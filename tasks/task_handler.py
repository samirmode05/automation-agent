from fastapi import HTTPException

def handle_task(task: str):
    
    if "install uv" in task and "run" in task:
        return install_and_run_uv(task)
    else:
        raise HTTPException(status_code=400, detail="Task not recognized or not supported yet")

def install_and_run_uv(task: str):
    import subprocess
    import os
    
    
    if "with" in task:
        user_email = task.split("with")[-1].strip()
    else:
        raise HTTPException(status_code=400, detail="Email not provided")

    
    try:
        subprocess.run(["pip", "show", "uv"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["pip", "install", "uv"], check=True)
    
    
    script_url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
    download_cmd = f"curl -o datagen.py {script_url}"
    os.system(download_cmd)
    run_cmd = f"python datagen.py {user_email}"
    os.system(run_cmd)

    return {"status": "Success", "message": f"datagen.py executed for {user_email}"}
