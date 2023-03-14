from typing import Union
import json
class extract:
    @staticmethod
    def extractDownloadableRaw(raw:Union[str,dict]):
        try:
            if not isinstance(raw, (str,dict)):
                raise AttributeError('signature given is not of str or dict type')
            
            if isinstance(raw, str):
                raw = json.loads(raw)

            if not isinstance(raw, (str,dict)):
                raise AttributeError('signature given is not of str or dict type')
        
        except Exception():
            raise AttributeError('signature not in proper format.')

        print('ok')

        