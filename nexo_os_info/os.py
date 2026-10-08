"""Operating system and system information utilities for Nexo OS Info."""

import ctypes
import os
import platform
import shutil
import socket
import time


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


def get_os_release():
    """Return the operating system release."""
    try:
        return platform.release() or "Unknown"
    except Exception:
        return "Unknown"


def get_platform():
    """Return Python's platform identifier."""
    try:
        return platform.platform() or "Unknown"
    except Exception:
        return "Unknown"


def get_kernel_version():
    """Return the kernel version reported by Python."""
    try:
        return platform.uname().version or "Unknown"
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


def get_cpu_count():
    """Return the number of logical CPU cores."""
    try:
        return os.cpu_count() or 0
    except Exception:
        return 0


def get_hostname():
    """Return the computer hostname."""
    try:
        return socket.gethostname() or "Unknown"
    except Exception:
        return "Unknown"


def get_memory():
    """Return total, available, used and free memory in bytes."""
    try:
        if is_windows():
            class MemoryStatus(ctypes.Structure):
                _fields_ = [
                    ("length", ctypes.c_ulong),
                    ("memory_load", ctypes.c_ulong),
                    ("total", ctypes.c_ulonglong),
                    ("available", ctypes.c_ulonglong),
                    ("page_file_total", ctypes.c_ulonglong),
                    ("page_file_available", ctypes.c_ulonglong),
                    ("virtual_total", ctypes.c_ulonglong),
                    ("virtual_available", ctypes.c_ulonglong),
                ]

            status = MemoryStatus()
            status.length = ctypes.sizeof(MemoryStatus)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
                return {
                    "total": status.total,
                    "available": status.available,
                    "used": status.total - status.available,
                    "free": status.available,
                }

        if is_linux():
            values = {}
            with open("/proc/meminfo", "r", encoding="utf-8") as file:
                for line in file:
                    key, value = line.split(":", 1)
                    values[key] = int(value.strip().split()[0]) * 1024

            total = values.get("MemTotal")
            available = values.get("MemAvailable", values.get("MemFree"))
            if total is not None and available is not None:
                return {
                    "total": total,
                    "available": available,
                    "used": total - available,
                    "free": available,
                }

        return {
            "total": None,
            "available": None,
            "used": None,
            "free": None,
        }
    except Exception:
        return {
            "total": None,
            "available": None,
            "used": None,
            "free": None,
        }


def get_disk_usage(path=None):
    """Return disk usage for a path in bytes."""
    try:
        target = path or os.path.abspath(os.sep)
        usage = shutil.disk_usage(target)
        return {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
        }
    except Exception:
        return {
            "total": None,
            "used": None,
            "free": None,
        }


def get_uptime():
    """Return system uptime in seconds when available."""
    try:
        if is_windows():
            return ctypes.windll.kernel32.GetTickCount64() / 1000.0

        if is_linux():
            with open("/proc/uptime", "r", encoding="utf-8") as file:
                return float(file.readline().split()[0])

        if is_macos():
            return time.monotonic()

        return time.monotonic()
    except Exception:
        return None


def get_system_info():
    """Return common operating system, hardware and runtime information."""
    memory = get_memory()
    return {
        "os": get_os_name(),
        "os_version": get_os_version(),
        "os_release": get_os_release(),
        "platform": get_platform(),
        "kernel_version": get_kernel_version(),
        "architecture": get_os_architecture(),
        "machine": get_machine_name(),
        "python": get_python_version(),
        "processor": get_processor(),
        "cpu_count": get_cpu_count(),
        "hostname": get_hostname(),
        "memory": memory,
        "uptime": get_uptime(),
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
