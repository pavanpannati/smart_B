from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')


def match_segments(transcript, brolls):
    results = []
    broll_texts = [b['description'] for b in brolls]
    broll_emb = model.encode(broll_texts, convert_to_tensor=True)


    for seg in transcript:
        seg_emb = model.encode(seg['text'], convert_to_tensor=True)
        scores = util.cos_sim(seg_emb, broll_emb)[0]
        best_idx = scores.argmax().item()
        confidence = scores[best_idx].item()


        if confidence > 0.45: # threshold
            results.append({
            "segment": seg,
            "broll_id": brolls[best_idx]['id'],
            "confidence": confidence
            })
    return results