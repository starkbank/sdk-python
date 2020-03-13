from re import compile


pattern = compile(r"(?<!^)(?=[A-Z0-9])")


def camel_to_snake(string):
    return pattern.sub("_", string).lower()


def snake_to_camel(string):
    split = string.split('_')
    return split[0] + "".join(word.title() for word in split[1:])


def camel_to_kebab(string):
    return pattern.sub("-", string).lower()
