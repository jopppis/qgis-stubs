# The PEP 484 type hints stub file for the _utils module.
#

from typing import Any

from . import gui as _gui

iface: _gui.QgisInterface
plugins: dict[str, Any]
plugins_metadata_parser: dict[str, Any]
