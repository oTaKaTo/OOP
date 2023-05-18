def update_records(record, id, property, value):
    if id in record:
        if property != "tracks" and value != '':
            record[id][property] = value
        elif property == 'tracks' and record[id].get("tracks") is None and value != '':
            record[id]["tracks"] = list(value)
        elif property == 'tracks' and value != '':
            record[id]["tracks"].append(value)
        elif value == '':
            record[id].pop(property)
    return record