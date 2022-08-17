from jsonschema import validate, ValidationError, SchemaError

def validate_json(json_data, json_schema):
    try:
        validate(instance=json_data, schema=json_schema)
        return True
    except:
        return False