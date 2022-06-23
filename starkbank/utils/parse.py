from .relay import set_relay
from starkcore.utils import parse


parse_and_verify = set_relay(parse.parse_and_verify)
