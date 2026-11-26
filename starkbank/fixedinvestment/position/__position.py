from starkcore.utils.subresource import SubResource


class Position(SubResource):
    """# fixedinvestment.Position object
    The fixedinvestment.Position object displays the consolidated position of your
    FixedInvestments between two dates. It is returned by fixedinvestment.position().
    ## Attributes (return-only):
    - initial_nominal_amount [integer]: nominal amount invested at the start date, in cents. ex: 161265163 (= R$ 1,612,651.63)
    - deposited_amount [integer]: amount deposited into investments in the period, in cents. ex: 1900000 (= R$ 19,000.00)
    - withdrawn_amount [integer]: amount withdrawn from investments in the period, in cents. ex: 417054 (= R$ 4,170.54)
    - yield_amount [integer]: gross yield in the period, in cents. ex: 81894 (= R$ 818.94)
    - final_nominal_amount [integer]: nominal amount invested at the end date, in cents. ex: 162829295 (= R$ 1,628,292.95)
    - ir_preview [integer]: preview of the income tax (IR) due, in cents. ex: 1256365 (= R$ 12,563.65)
    - regressive_and_fee_preview [integer]: preview of the regressive tax and fees due, in cents. ex: 3824 (= R$ 38.24)
    """

    def __init__(self, initial_nominal_amount, deposited_amount, withdrawn_amount, yield_amount, final_nominal_amount,
                 ir_preview, regressive_and_fee_preview):
        self.initial_nominal_amount = initial_nominal_amount
        self.deposited_amount = deposited_amount
        self.withdrawn_amount = withdrawn_amount
        self.yield_amount = yield_amount
        self.final_nominal_amount = final_nominal_amount
        self.ir_preview = ir_preview
        self.regressive_and_fee_preview = regressive_and_fee_preview


_sub_resource = {"class": Position, "name": "Position"}
