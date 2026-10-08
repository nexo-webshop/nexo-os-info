# Nexo OS Info

[![PyPI](https://img.shields.io/pypi/v/nexo-os-info)](https://pypi.org/project/nexo-os-info/)
[![Python](https://img.shields.io/pypi/pyversions/nexo-os-info)](https://pypi.org/project/nexo-os-info/)

**Nexo OS Info** is a lightweight Python library for retrieving useful operating-system, hardware and runtime information.

## Installation

```bash
python -m pip install nexo-os-info
```

Upgrade with:

```bash
python -m pip install --upgrade nexo-os-info
```

## Quick start

```python
from nexo_os_info import get_system_info

info = get_system_info()

for key, value in info.items():
    print(f"{key}: {value}")
```

## Available functions

### Operating system

- `get_os_name()` — operating-system name.
- `get_os_version()` — operating-system version.
- `get_os_release()` — operating-system release.
- `get_platform()` — Python platform identifier.
- `get_kernel_version()` — kernel version.
- `get_os_architecture()` — `32bit` or `64bit`.
- `get_machine_name()` — machine architecture identifier.

### Hardware

- `get_processor()` — processor information when available.
- `get_cpu_count()` — logical CPU count.
- `get_memory()` — total, available, used and free memory in bytes.
- `get_disk_usage(path=None)` — total, used and free disk space for a path.

### Runtime and network identity

- `get_python_version()` — Python version.
- `get_hostname()` — computer hostname.
- `get_uptime()` — system uptime in seconds when available.

### Detection helpers

- `is_windows()`
- `is_linux()`
- `is_macos()`

### Combined information

`get_system_info()` returns:

```text
os
os_version
os_release
platform
kernel_version
architecture
machine
python
processor
cpu_count
hostname
memory
uptime
```

The `memory` value is a dictionary with `total`, `available`, `used` and `free` in bytes.

## Example

```python
from nexo_os_info import get_memory, get_cpu_count, get_uptime

print(f"CPU threads: {get_cpu_count()}")
print(f"Memory: {get_memory()}")
print(f"Uptime: {get_uptime()} seconds")
```

## Lightweight by design

Nexo OS Info intentionally has **no third-party runtime dependency** for these features. Windows memory and uptime use native Windows APIs, Linux memory and uptime use procfs, and common platform information uses Python's standard library.

It is not intended to be a full hardware-monitoring suite, task manager or benchmarking framework.

## Reliability

Information can differ between operating systems and execution environments. Functions therefore use safe fallbacks such as `"Unknown"`, `0`, `None`, or dictionaries containing `None` values where information cannot be retrieved.

## Development status

Current version: **0.0.1.6**

The project is still in **Alpha**. The public API may change before 1.0.0.

Nexo OS Info is developed by **Nexo Studios**.

---

**Nexo Studios — Building Tomorrow Together.**
