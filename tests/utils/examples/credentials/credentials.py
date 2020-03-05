from json import loads

from ellipticcurve.utils.file import File
credentialsJson = loads(File.read("utils/examples/credentials/development.json"))
