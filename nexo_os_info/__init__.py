"""
Nexo OS Info
A simple Python package for retrieving operating system and system information.
"""

from .os import (
    get_os_name,
    get_os_version,
    get_os_architecture,
    get_machine_name,
    get_python_version,
    get_processor,
    get_hostname,
    get_system_info,
    is_windows,
    is_linux,
    is_macos,
)

from .github import get_changelog

__version__ = "0.0.1.4"

__all__ = [
    "get_os_name",
    "get_os_version",
    "get_os_architecture",
    "get_machine_name",
    "get_python_version",
    "get_processor",
    "get_hostname",
    "get_system_info",
    "is_windows",
    "is_linux",
    "is_macos",
    "get_changelog",
]
