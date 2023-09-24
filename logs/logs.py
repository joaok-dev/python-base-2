#!usr/bin/env python3

import logging
import os

# BOILER PLATE
# TODO: use function
# TODO: use lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# out instance
log = logging.Logger(__name__, log_level)
# level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# formatting
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)
ch.setFormatter(fmt)
# destination
log.addHandler(ch)

log.debug("Mesage to dev, qe, sysadmin")
log.info("General message to user")
log.warning("Warning that causes error")
log.error("Error that affect a single execution")
log.critical("General Error. Ex: Database missing")

print("-" * 12)
