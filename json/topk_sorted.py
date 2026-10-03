data = [
    {"id": "A", "score": 0.72},
    {"id": "B", "score": 0.91},
    {"id": "C", "score": 0.83}
]

data = sorted(data, key=lambda x: x["score"],reverse=True)[:2]
for d in data:
    print(d['id'],d['score'])
