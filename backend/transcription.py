import whisper


model = whisper.load_model("base")


def transcribe_video(video_path):
    result = model.transcribe(video_path)
    transcript = []
    for seg in result['segments']:
        transcript.append({
        "start": seg['start'],
        "end": seg['end'],
        "text": seg['text']
        })
    return transcript