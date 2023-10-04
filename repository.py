def get_message_ids(cursor, discussion_id):
    sql_request = """
        SELECT t3.id
        FROM discussion_messages as t1
        LEFT JOIN discussion as t2 ON t1.discussion_id = t2.id
        LEFT JOIN message as t3 ON t1.message_id = t3.id
        WHERE t2.id = %s
        order by id asc
    """
    cursor.execute(sql_request, (discussion_id,))
    return [item[0] for item in cursor.fetchall()]

# TODO добавить summary, name, goal, is_goal_achieved


def get_messages(cursor, start_msg, end_msg):
    sql_request = """
        SELECT id, message.date, message.from_name, message.text
        FROM message
        WHERE id > %s and id < %s;
    """
    start_msg -= 6
    end_msg += 6
    cursor.execute(sql_request, (start_msg, end_msg,))
    return cursor.fetchall()
