"""
Operating system and system information utilities for Nexo OS Info.
"""

import platform
import socket


def get_os_name():
    """Return the name of the current operating system."""
    try:
        return platform.system() or "Unknown"
    except Exception:
        return "Unknown"


def get_os_version():
    """Return the current operating system version."""
    try:
        return platform.version() or "Unknown"
    except Exception:
        return "Unknown"


def get_os_architecture():
    """Return the operating system architecture."""
    try:
        return platform.architecture()[0] or "Unknown"
    except Exception:
        return "Unknown"


def get_machine_name():
    """Return the machine hardware identifier."""
    try:
        return platform.machine() or "Unknown"
    except Exception:
        return "Unknown"


def get_python_version():
    """Return the current Python version."""
    try:
        return platform.python_version() or "Unknown"
    except Exception:
        return "Unknown"


def get_processor():
    """Return processor information."""
    try:
        return platform.processor() or "Unknown"
    except Exception:
        return "Unknown"


def get_hostname():
    """Return the computer hostname."""
    try:
        return socket.gethostname() or "Unknown"
    except Exception:
        return "Unknown"


def get_system_info():
    """Return common operating system and system information."""
    return {
        "os": get_os_name(),
        "os_version": get_os_version(),
        "architecture": get_os_architecture(),
        "machine": get_machine_name(),
        "python": get_python_version(),
        "processor": get_processor(),
        "hostname": get_hostname(),
    }


def is_windows():
    """Return True if the current operating system is Windows."""
    return get_os_name().lower() == "windows"


def is_linux():
    """Return True if the current operating system is Linux."""
    return get_os_name().lower() == "linux"


def is_macos():
    """Return True if the current operating system is macOS."""
    return get_os_name().lower() == "darwin"
