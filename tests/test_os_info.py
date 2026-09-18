"""Tests for Nexo OS Info."""

import platform

import nexo_os_info
from nexo_os_info.os import (
    get_hostname,
    get_machine_name,
    get_os_architecture,
    get_os_name,
    get_os_version,
    get_processor,
    get_python_version,
    get_system_info,
    get_uptime,
    is_linux,
    is_macos,
    is_windows,
)


def test_version():
    assert nexo_os_info.__version__ == "0.0.1.5"


def test_os_name():
    assert get_os_name() == platform.system()


def test_os_version():
    assert get_os_version() == platform.version()


def test_os_architecture():
    assert get_os_architecture() in {"32bit", "64bit", "Unknown"}


def test_machine_name():
    assert isinstance(get_machine_name(), str)
    assert get_machine_name()


def test_python_version():
    assert get_python_version() == platform.python_version()


def test_processor():
    assert isinstance(get_processor(), str)


def test_hostname():
    assert isinstance(get_hostname(), str)
    assert get_hostname()


def test_system_info():
    info = get_system_info()
    assert isinstance(info, dict)
    assert set(info) == {
        "os",
        "os_version",
        "architecture",
        "machine",
        "python",
        "processor",
        "hostname",
    }


def test_platform_detection():
    name = get_os_name().lower()
    assert is_windows() is (name == "windows")
    assert is_linux() is (name == "linux")
    assert is_macos() is (name == "darwin")


def test_uptime():
    uptime = get_uptime()
    assert uptime is None or isinstance(uptime, (int, float))
    if uptime is not None:
        assert uptime >= 0


def test_uptime_increases():
    first = get_uptime()
    second = get_uptime()
    if first is not None and second is not None:
        assert second >= first
