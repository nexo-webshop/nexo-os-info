"""Tests for Nexo OS Info."""

import platform

import nexo_os_info
from nexo_os_info.os import (
    get_cpu_count, get_disk_usage, get_hostname, get_kernel_version,
    get_machine_name, get_memory, get_os_architecture, get_os_name,
    get_os_release, get_os_version, get_platform, get_processor,
    get_python_version, get_system_info, get_uptime,
    is_linux, is_macos, is_windows,
)


def test_version():
    assert nexo_os_info.__version__ == "0.0.1.6"


def test_os_name():
    assert get_os_name() == platform.system()


def test_os_version():
    assert get_os_version() == platform.version()


def test_os_release():
    assert isinstance(get_os_release(), str)
    assert get_os_release()


def test_platform():
    assert isinstance(get_platform(), str)
    assert get_platform()


def test_kernel_version():
    assert isinstance(get_kernel_version(), str)
    assert get_kernel_version()


def test_os_architecture():
    assert get_os_architecture() in {"32bit", "64bit", "Unknown"}


def test_machine_name():
    assert isinstance(get_machine_name(), str)
    assert get_machine_name()


def test_python_version():
    assert get_python_version() == platform.python_version()


def test_processor():
    assert isinstance(get_processor(), str)


def test_cpu_count():
    assert isinstance(get_cpu_count(), int)
    assert get_cpu_count() >= 0


def test_hostname():
    assert isinstance(get_hostname(), str)
    assert get_hostname()


def test_memory():
    memory = get_memory()
    assert set(memory) == {"total", "available", "used", "free"}
    assert all(value is None or isinstance(value, int) for value in memory.values())
    if memory["total"] is not None and memory["available"] is not None:
        assert memory["total"] >= memory["available"] >= 0


def test_disk_usage():
    disk = get_disk_usage()
    assert set(disk) == {"total", "used", "free"}
    assert all(value is None or isinstance(value, int) for value in disk.values())


def test_system_info():
    info = get_system_info()
    assert isinstance(info, dict)
    assert set(info) == {
        "os", "os_version", "os_release", "platform", "kernel_version",
        "architecture", "machine", "python", "processor", "cpu_count",
        "hostname", "memory", "uptime",
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
