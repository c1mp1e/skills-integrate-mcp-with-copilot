"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import os
from pathlib import Path
import json
import threading
from typing import Dict, Any

app = FastAPI(
    title="Mergington High School API",
    description="API for viewing and signing up for extracurricular activities",
)

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(Path(__file__).parent, "static")),
    name="static",
)

# Data file for activities (moves activities out of source code)
ACTIVITIES_FILE = current_dir / "activities.json"
_lock = threading.Lock()


def load_activities() -> Dict[str, Any]:
    if ACTIVITIES_FILE.exists():
        try:
            with ACTIVITIES_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_activities(data: Dict[str, Any]) -> None:
    with _lock:
        with ACTIVITIES_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


# Initialize activities from file (or keep empty dict if not present)
activities = load_activities()


class SignupRequest(BaseModel):
    email: EmailStr


class UnregisterRequest(BaseModel):
    email: EmailStr


# Allow CORS from local frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, body: SignupRequest = Body(...)):
    """Sign up a student for an activity. Accepts JSON body: {"email": "..."}."""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    # Validate student is not already signed up
    if body.email in activity.get("participants", []):
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Validate capacity
    maxp = activity.get("max_participants")
    if isinstance(maxp, int) and len(activity.get("participants", [])) >= maxp:
        raise HTTPException(status_code=400, detail="Activity is full")

    # Add student
    with _lock:
        activity.setdefault("participants", []).append(body.email)
        save_activities(activities)

    return JSONResponse(status_code=201, content={"message": f"Signed up {body.email} for {activity_name}"})


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, body: UnregisterRequest = Body(...)):
    """Unregister a student from an activity. Accepts JSON body: {"email": "..."}."""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    # Validate student is signed up
    if body.email not in activity.get("participants", []):
        raise HTTPException(status_code=400, detail="Student is not signed up for this activity")

    # Remove student
    with _lock:
        activity.get("participants", []).remove(body.email)
        save_activities(activities)

    return {"message": f"Unregistered {body.email} from {activity_name}"}
