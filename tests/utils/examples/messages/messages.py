import os
from json import loads

from ellipticcurve.utils.file import File

dir = os.path.dirname(os.path.abspath(__file__))

exampleBoletosJson = loads(File.read(os.path.join(dir, "exampleBoleto.json")))
exampleBoletoPaymentsJson = loads(File.read(os.path.join(dir, "exampleBoletoPayment.json")))
exampleTransfersJson = loads(File.read(os.path.join(dir, "exampleTransfer.json")))
exampleTransactionsJson = loads(File.read(os.path.join(dir, "exampleTransaction.json")))
exampleUtilityPaymentsJson = loads(File.read(os.path.join(dir, "exampleUtilityPayment.json")))
