class ApiError(Exception):
    def __init__(self, code, message):
        super(Exception, self).__init__(message)
        self.code = code
        self.message = message


class InputError(ApiError):
    def __init__(self, code, message):
        super(Exception, self).__init__("{code}: {message}".format(code=code, message=message))
        self.code = code
        self.message = message


class Houston(Exception):
    def __init__(self, message="Internal server error"):
        super(Exception, self).__init__(message)
