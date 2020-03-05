from json import loads

from ellipticcurve.utils.file import File

exampleBoletosJson = loads(File.read("utils/examples/messages/exampleBoleto.json"))
exampleBoletoPaymentsJson = loads(File.read("utils/examples/messages/exampleBoletoPayment.json"))
exampleTransfersJson = loads(File.read("utils/examples/messages/exampleTransfer.json"))
exampleTransactionsJson = loads(File.read("utils/examples/messages/exampleInternalTransaction.json"))