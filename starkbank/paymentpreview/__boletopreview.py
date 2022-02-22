from starkcore.utils.subresource import SubResource


class BoletoPreview(SubResource):

    """# BoletoPreview object
    A BoletoPreview is used to get information from a Boleto payment you received before confirming the payment.
    ## Attributes (return-only):
    - status [string]: current boleto status. ex: "active", "expired" or "inactive"
    - amount [int]: final amount to be paid. ex: 23456 (= R$ 234.56)
    - discount_amount [int]: discount amount to be paid. ex: 23456 (= R$ 234.56)
    - fine_amount [int]: fine amount to be paid. ex: 23456 (= R$ 234.56)
    - interest_amount [int]: interest amount to be paid. ex: 23456 (= R$ 234.56)
    - due [datetime.date]: Boleto due date. ex: 2020-04-30
    - expiration [datetime.date]: Boleto expiration date. ex: 2020-04-30
    - name [string]: beneficiary full name. ex: "Anthony Edward Stark"
    - tax_id [string]: beneficiary tax ID (CPF or CNPJ). ex: "20.018.183/0001-80"
    - receiver_name [string]: receiver (Sacador Avalista) full name. ex: "Anthony Edward Stark"
    - receiver_tax_id [string]: receiver (Sacador Avalista) tax ID (CPF or CNPJ). ex: "20.018.183/0001-80"
    - payer_name [string]: payer full name. ex: "Anthony Edward Stark"
    - payer_tax_id [string]: payer tax ID (CPF or CNPJ). ex: "20.018.183/0001-80"
    - line [string]: Number sequence that identifies the payment. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
    - bar_code [string]: Bar code number that identifies the payment. ex: "34195819600000000621090063571277307144464000"
    """

    def __init__(self, status, amount, discount_amount, fine_amount, interest_amount, due, expiration, name, tax_id,
                 receiver_name, receiver_tax_id, payer_name, payer_tax_id, line, bar_code):
        self.status = status
        self.amount = amount
        self.discount_amount = discount_amount
        self.fine_amount = fine_amount
        self.interest_amount = interest_amount
        self.due = due
        self.expiration = expiration
        self.name = name
        self.tax_id = tax_id
        self.receiver_name = receiver_name
        self.receiver_tax_id = receiver_tax_id
        self.payer_name = payer_name
        self.payer_tax_id = payer_tax_id
        self.line = line
        self.bar_code = bar_code


_sub_resource = {"class": BoletoPreview, "name": "BoletoPreview"}
