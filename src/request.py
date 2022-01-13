import json
from json.encoder import JSONEncoder
#enum
class requestType():
        AUTH = 0
        ADD = 1
        DELETE = 2
        GET = 3
        GRANT = 4
        EDIT = 5
        SEARCH = 6
        QUIT = 7

class request():
    rtype : requestType
    rparameters : list
    
    def __init__(self, rtype, rparameters):
            self.rtype = rtype
            self.rparameters = rparameters
    
    def dump(self):
            def encoder(obj):
                if isinstance(obj, request):
                        return {"__class__": "request",
                                "rtype": obj.rtype,
                                "rparameters": obj.rparameters}
                raise TypeError(repr(obj) + " is not JSON serializable")

            dump = json.dumps(self, default=encoder)
            return dump

    def load(string):
            def decoder(obj_dict):
                if "__class__" in obj_dict:
                        if obj_dict["__class__"] == "request":
                                obj = request(objet["rtype"])
                                obj.rparameters = objet["raparameters"]
                                return obj
                return objet
            self = json.loads(string, object_hook=decoder)
        
    
