sorted_data = sorted(
    json,
    key=lambda x: x['similarity_score'],
    reverse=True
)

selected_docs = set()

for data in sorted_data:
    if data['doc_id'] not in selected_docs:
        print(data['query_id'], data['doc_id'])
        selected_docs.add(data['doc_id'])

    if len(selected_docs) == 2:
        break
