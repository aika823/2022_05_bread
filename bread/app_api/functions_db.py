import json

def format_data(field_name):
    # open json file
    with open('model_data.json', encoding="UTF-8") as json_file:
        model_data = json.load(json_file)
    try:
        if model_data[field_name]:
            model_data[field_name]['name'] = field_name
            return model_data[field_name]
    except:
        return None

def get_field_list(model):
    return [format_data(field.name) for field in model._meta.get_fields() if format_data(field.name)]

def get_values(object):
    field_list = get_field_list(object._meta.model)
    for field in field_list:
        field['value'] = getattr(object, field['name'])
    return field_list