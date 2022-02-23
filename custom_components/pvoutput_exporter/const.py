"""Constants for the PVOutput Exporter integration."""
from __future__ import annotations

from typing import Final

DOMAIN = "pvoutput_exporter"

ATTR_ENTRY_TYPE: Final = "entry_type"
ENTRY_TYPE_SERVICE: Final = "service"

ATTRIBUTION: Final = "Data sent to PV Output"

CONF_SYSTEM_ID = "system_id"

PV_OUTPUT_API_URL = "https://pvoutput.org/service/r2/addoutput.jsp"
