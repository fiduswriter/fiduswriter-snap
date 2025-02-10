#!/usr/bin/env python3
import os
import sys
from subprocess import call
from urllib.parse import urlparse

SNAP = os.environ.get("SNAP")
SNAP_DATA = os.environ.get("SNAP_DATA")

if __name__ == "__main__":
    if os.getuid() != 0:
        print("This script must be run by root")
        sys.exit()

    sys.path.append(SNAP_DATA)
    try:
        import configuration
        if 'pandoc' not in configuration.INSTALLED_APPS:
            sys.exit(0)
        pandoc_url = "http://localhost:3030/"
        if hasattr(configuration, "PANDOC_URL"):
            pandoc_url = configuration.PANDOC_URL
        parsed = urlparse(pandoc_url)
        hostname, port = parsed.hostname, parsed.port
        if hostname not in ["localhost", "127.0.0.1"]:
            sys.exit(0)
        call([
            f"{SNAP}/bin/pandoc",
            "server",
            f"-p {port}"
        ])
    except ModuleNotFoundError:
        sys.exit(0)
