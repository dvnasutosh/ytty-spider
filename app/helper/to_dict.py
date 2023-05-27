from enum import Enum


def to_raw_dict(obj: object, processed=None):
    if processed is None:
        processed = set()
    if id(obj) in processed:
        return "<circular reference>"
    processed.add(id(obj))
    if isinstance(obj, dict):
        out = dict()
        for key, value in obj.items():
            if isinstance(value, dict):
                out[key] = to_raw_dict(value, processed)
            elif isinstance(value, Enum):
                out[key] = [str(value), value.value]
            elif isinstance(value, (list, tuple, set)):
                out[key] = to_raw_dict(value, processed)
            elif isinstance(value, (int, float, bool, complex, str)):
                out[key] = value
            elif isinstance(value, object):
                out[key] = to_raw_dict(value.__dict__, processed)
            else:
                out[key] = str(value)
        return out
    elif isinstance(obj, (list, tuple, set)):
        l = []
        for item in obj:
            l.append(to_raw_dict(item, processed))
        return l
    elif isinstance(obj, (int, float, bool, complex, str)):
        return obj
    elif isinstance(obj, Enum):
        return [str(value), value.value]
    elif isinstance(obj, object):
        return to_raw_dict(obj.__dict__, processed)
    else:
        return str(obj)
