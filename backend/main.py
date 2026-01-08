from fastapi import FastAPI
from transcription import transcribe_video
from broll_analysis import analyze_broll
from matcher import match_segments
from planner import build_timeline
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-plan")
def generate_plan():
    with open("data/video_url.json") as f:
        data = json.load(f)

    timeline = {
    "a_roll_duration": 40.3,
    "insertions": [
        {
            "start_sec": 29.9,
            "duration_sec": 0.6,
            "broll_id": "broll_2"
        }]}

    
    a_roll_url = data["a_roll"]["url"]

    transcript = transcribe_video(a_roll_url)
    brolls = analyze_broll(data['b_rolls'])
    matches = match_segments(transcript, brolls)
    timeline = build_timeline(matches)


    return {
    "a_roll_duration": transcript[-1]['end'],
    "insertions": timeline
    }