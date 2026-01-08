def build_timeline(matches, max_inserts=5):
    timeline = []
    used = set()


    for m in matches:
        if len(timeline) >= max_inserts:
            break
        if m['broll_id'] in used:
            continue


        duration = min(3.0, m['segment']['end'] - m['segment']['start'])


        timeline.append({
        "start_sec": m['segment']['start'],
        "duration_sec": duration,
        "broll_id": m['broll_id'],
        "confidence": round(m['confidence'], 2),
        "reason": f"Matches visual context of: {m['segment']['text']}"
        })
        used.add(m['broll_id'])


    return timeline