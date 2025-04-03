version = "2.28.1"

user = None
language = "en-US"
timeout = 15
request_methods_prefix = "Joker"

from starkcore import Organization, Project

from . import error
from . import key

from . import transaction
from .transaction.__transaction import Transaction

from . import balance
from .balance.__balance import Balance

from . import boleto
from .boleto.__boleto import Boleto

from . import transfer
from .transfer.__transfer import Transfer

from . import institution
from .institution.__institution import Institution

from . import boletoholmes
from .boletoholmes.__boletoholmes import BoletoHolmes

from . import brcodepayment
from .brcodepayment.__brcodepayment import BrcodePayment

from . import boletopayment
from .boletopayment.__boletopayment import BoletoPayment

from . import corporatetransaction
from .corporatetransaction.__corporatetransaction import CorporateTransaction

from . import corporateholder
from .corporateholder.__corporateholder import CorporateHolder

from . import corporatebalance
from .corporatebalance.__corporatebalance import CorporateBalance

from . import corporatecard
from .corporatecard.__corporatecard import CorporateCard

from . import corporatepurchase
from .corporatepurchase.__corporatepurchase import CorporatePurchase

from . import corporateinvoice
from .corporateinvoice.__corporateinvoice import CorporateInvoice

from . import corporatewithdrawal
from .corporatewithdrawal.__corporatewithdrawal import CorporateWithdrawal

from . import corporaterule
from .corporaterule.__corporaterule import CorporateRule

from . import merchantcard
from .merchantcard.__merchantcard import MerchantCard

from . import merchantcategory
from .merchantcategory.__merchantcategory import MerchantCategory

from . import merchantcountry
from .merchantcountry.__merchantcountry import MerchantCountry

from . import merchantinstallment
from .merchantinstallment.__merchantinstallment import MerchantInstallment

from . import merchantpurchase
from .merchantpurchase.__merchantpurchase import MerchantPurchase

from . import merchantsession
from .merchantsession.__merchantsession import MerchantSession

from . import cardmethod
from .cardmethod.__cardmethod import CardMethod

from . import utilitypayment
from .utilitypayment.__utilitypayment import UtilityPayment

from . import taxpayment
from .taxpayment.__taxpayment import TaxPayment

from . import darfpayment
from .darfpayment.__darfpayment import DarfPayment

from . import webhook
from .webhook.__webhook import Webhook

from . import workspace
from .workspace.__workspace import Workspace

from . import event
from .event.__event import Event

from . import paymentpreview
from .paymentpreview.__paymentpreview import PaymentPreview

from . import paymentrequest
from .paymentrequest.__paymentrequest import PaymentRequest

from . import invoice
from .invoice.__invoice import Invoice

from . import dictkey
from .dictkey.__dictkey import DictKey

from . import dynamicbrcode
from .dynamicbrcode.__dynamicbrcode import DynamicBrcode

from . import deposit
from .deposit.__deposit import Deposit

from . import split
from .split.__split import Split

from . import splitreceiver
from .splitreceiver.__splitreceiver import SplitReceiver

from . import splitprofile
from .splitprofile.__splitprofile import SplitProfile

from . import request

