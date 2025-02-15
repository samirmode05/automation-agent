import os
from fastapi import APIRouter

router = APIRouter()

@router.post("/run/task_A1")
def run_task_A1(email: str):
    # Install uv if not already installed
    os.system("pip install uv")

    # Download and run the script with the provided email
    os.system("curl -O https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py")
    os.system(f"python datagen.py {24f1001198@ds.study.iitm.ac.in}")

    return {"status": "Task A1 completed"}
