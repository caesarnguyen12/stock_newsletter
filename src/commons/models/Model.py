
class Model:
    # {parameter_name: type}
    ALLOWED = {}


    def __init__(self, **kwargs):
        self.parameters = {}
        for k, v in self.ALLOWED:
            parameter = kwargs.get(k)
            if parameter:
                if type(parameter) == v:
                    self.parameters[k] = parameter
                else:
                    # TODO: migrate to exceptions
                    raise Exception("Model Data Does Not Match")


    def getParams(self, key=None):
        if key:
            return self.parameters[key]
        return self.parameters

    def getHeaders(self):
        return list(self.parameters.keys())
