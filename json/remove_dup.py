data = [
    {"doc_id": "D1", "score": 0.9},
    {"doc_id": "D2", "score": 0.8},
    {"doc_id": "D1", "score": 0.7},
    {"doc_id": "D3", "score": 0.6}
]
data = sorted(data,key = lambda x:x['score'],reverse=True)
s = set()
for d in data:
    if d['doc_id'] in s:
        continue
    else:
        print(d["doc_id"],d['score'])
        s.add(d['doc_id'])
