

class ErrorElement(Exception):
    def __init__(self, code, message):
        super(Exception, self).__init__("{code}: {message}".format(code=code, message=message))
        self.code = code
        self.message = message


class InputErrors(Exception):
    def __init__(self, content):
        self.elements = [ErrorElement(code=error["code"], message=error["message"]) for error in content]
        super(Exception, self).__init__(str(content))


class Houston(Exception):
    def __init__(self, message="Internal server error"):
        super(Exception, self).__init__(message)


class UnknownException(Exception):
    def __init__(self, message):
        super(Exception, self).__init__("Unknown exception encountered: {}".format(message))
