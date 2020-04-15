

class Enum:

    @classmethod
    def values(cls):
        return [attribute for attribute in dir(cls) if not attribute.startswith('_') and not callable(getattr(cls, attribute))]

    @classmethod
    def is_valid(cls, item):
        return item in cls.values()
