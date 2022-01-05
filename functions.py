from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

def get_dict(obj_):
    dict_ = [object_as_dict(item) for item in obj_]
    return dict_

