from enum import Enum
import json
def to_raw_dict(obj:object):
    if isinstance(obj, dict):
        out=dict()
        
        for key,value in obj.items():

            if isinstance(value, dict):
                out[key]=to_raw_dict(value)
        
            elif isinstance(value, Enum):
                out[key]=[str(value),value.value]
        
            elif isinstance(value,(list,tuple,set)):
            
                out[key]=to_raw_dict(value)

            elif isinstance(value, (int,float,bool,complex,str)):
                out[key]=value


            elif isinstance(value, object):
                if hasattr(value, '__json__'):
                    out[key]=json.loads(value.__json__())
                else:
                    out[key]=to_raw_dict(value.__dict__)
            else:
                out[key]=str(value)
        return out    

    elif isinstance(obj, (list,tuple,set)):
        l=list()
        for item in obj:
            l.append(to_raw_dict(item))
        return l
    elif isinstance(obj, (int,float,bool,complex,str)):
        return obj
    elif isinstance(obj, Enum):
        return [str(value),value.value]
    elif isinstance(obj, object):
        if hasattr(obj, '__json__'):
            return json.loads(obj.__json__())
        else:
            return to_raw_dict(obj.__dict__)
    else:
        return str(obj)
        
