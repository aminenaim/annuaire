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
    
    

