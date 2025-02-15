#!/usr/bin/env python3
import ipaddress
import sys
import os
import configuration

SNAP_DATA = os.environ.get("SNAP_DATA")
CONFIGURE_PATH = "{}/configuration.py".format(SNAP_DATA)

if not os.path.isfile(CONFIGURE_PATH):
    sys.exit(0)


def is_ipaddress(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


with open(CONFIGURE_PATH) as f:
    configuration_str = f.read()
sys.path.append(SNAP_DATA)

configuration_str += "\n"
configuration_str += "\n# Fidus Writer 3.11.0 addition"
configuration_str += "\nCSRF_TRUSTED_ORIGINS = ["

if hasattr(configuration, "ALLOWED_HOSTS") and type(
    configuration.ALLOWED_HOSTS
) in [
    list,
    tuple,
]:
    for allowed_host in configuration.ALLOWED_HOSTS:
        if (
            type(allowed_host) is str
            and "localhost" not in allowed_host
            and not is_ipaddress(allowed_host)
            and allowed_host != "*"
        ):
            configuration_str += f"'https://{'*' if allowed_host.startswith('.') else ''}{allowed_host}', "

configuration_str += "]\n"

with open(CONFIGURE_PATH, "w") as f:
    f.write(configuration_str)
