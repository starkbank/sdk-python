from .relay import set_relay
from starkcore.utils import rest


get_page = set_relay(rest.get_page)
get_stream = set_relay(rest.get_stream)
get_id = set_relay(rest.get_id)
get_content = set_relay(rest.get_content)
get_sub_resource = set_relay(rest.get_sub_resource)
get_sub_resources = set_relay(rest.get_sub_resources)
post_sub_resource = set_relay(rest.post_sub_resource)
post_multi = set_relay(rest.post_multi)
post_single = set_relay(rest.post_single)
delete_id = set_relay(rest.delete_id)
get_raw = set_relay(rest.get_raw)
post_raw = set_relay(rest.post_raw)
patch_id = set_relay(rest.patch_id)
put_multi = set_relay(rest.put_multi)
put_raw = set_relay(rest.put_raw)
patch_raw = set_relay(rest.patch_raw)
delete_raw = set_relay(rest.delete_raw)
