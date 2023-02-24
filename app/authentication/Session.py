import uuid
import datetime

import random

class Session:
    
    def generate_uuid():
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        rand = str(random.getrandbits(64))
        input = timestamp  + rand
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, input))

    