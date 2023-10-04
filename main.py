import logging
import os
import json

from repository import get_messages, get_message_ids
from discussion_parser import verify_discussion, create_label_studio_data

import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode="w",
    filename="logs.txt",
    encoding="UTF-8"
)

if __name__ == "__main__":
    logging.info("Connecting to database.")
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    logging.info("Connected to database.")
    to_file = []
    for discussion_id in range(285, 320):
        ids = get_message_ids(cursor, discussion_id)
        if ids:
            data = get_messages(cursor, ids[0], ids[-1])
            updated_data = verify_discussion(ids, data)
            studio_data = create_label_studio_data(discussion_id, updated_data)
            to_file.append(studio_data)
    with open("label_studio_data.json", "w", encoding="utf-8") as file:
        json_data = json.dumps(to_file, ensure_ascii=False)
        file.write(json_data)
    conn.close()
    logging.info("Connection closed.")
