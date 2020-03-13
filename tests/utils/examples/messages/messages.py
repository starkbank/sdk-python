from json import loads

from ellipticcurve.utils.file import File

exampleBoletosJsonString = loads(File.read("utils/examples/messages/exampleBoleto.json"))
exampleBoletoPaymentsJson = loads(File.read("utils/examples/messages/exampleBoletoPayment.json"))
exampleTransfersJsonString = loads(File.read("utils/examples/messages/exampleTransfer.json"))
exampleTransactionsJson = loads(File.read("utils/examples/messages/exampleTransaction.json"))
exampleUtilityPaymentsJsonString = loads(File.read("utils/examples/messages/exampleUtilityPayment.json"))
