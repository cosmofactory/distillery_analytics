def verify_discussion(ids, data):
    new_data = []
    for id in data:
        temp = []
        temp.extend(x for x in id)
        if id[0] in ids:
            temp[3] = "🍏" + id[3]
        new_data.append(tuple(temp))
    return new_data


def create_label_studio_data(discussion_id, updated_data):
    data = {"extended_discussion": f"### This is discussion № {discussion_id} ###\n"}
    for item in updated_data:
        items = ": ".join(str(x) for x in item)
        data["extended_discussion"] += items + "\n"
    return data
