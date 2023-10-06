import csv
import json
from collections import defaultdict


def parse_csv_and_save_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        grouped_data = defaultdict(list)

        for row in reader:
            try:
                history = json.loads(row['History'].replace('""', '"'))
                content = history['data']['content'].encode('utf-8').decode('unicode_escape')
                grouped_data[row['SessionId']].append((history['type'], content))
            except Exception as e:
                print(f"Failed to process row {row['_id']}: {str(e)}")

    output_data = []
    for session_id, messages in grouped_data.items():
        session_data = "\n".join([f"{msg_type}: {content}" for msg_type, content in messages])
        output_data.append({"session": session_data})

    with open(json_file_path, mode='w', encoding='ISO-8859-1') as json_file:
        json.dump(output_data, json_file, ensure_ascii=False, indent=2)


parse_csv_and_save_json('csv_parser/message_store_202310051505.csv', 'csv_parser/output.json')
