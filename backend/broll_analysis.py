def analyze_broll(brolls):
    analyzed = []
    for b in brolls:
        analyzed.append({
        "id": b['id'],
        "description": b['metadata']
        })
    return analyzed