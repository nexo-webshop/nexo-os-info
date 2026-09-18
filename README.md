# Nexo OS Info

[![PyPI](https://img.shields.io/pypi/v/nexo-os-info)](https://pypi.org/project/nexo-os-info/)
[![Python](https://img.shields.io/pypi/pyversions/nexo-os-info)](https://pypi.org/project/nexo-os-info/)
[![License](https://img.shields.io/badge/license-see%20repository-blue)](https://github.com/nexo-webshop/nexo-os-info)

**Nexo OS Info** is a lightweight Python library for retrieving useful operating-system and computer information with simple Python functions.

Instead of writing your own collection of `platform`, `socket`, and operating-system checks every time, Nexo OS Info gives you one small, straightforward API.

> ⚠️ **Development status:** Nexo OS Info is actively developed. Some functionality may change before version 1.0.0. The project is currently intended for developers who are comfortable using a library that is still evolving.

## Why Nexo OS Info?

System information is useful in many Python projects:

- desktop applications
- diagnostics and support tools
- system dashboards
- hardware and software information screens
- installers and setup tools
- compatibility checks
- development utilities
- Nexo Studios projects

The goal is simple: **make common system-information tasks easy without making the library unnecessarily large.**

Nexo OS Info focuses on a small API and avoids turning a basic information library into a huge dependency-heavy package.

## Installation

Install the latest published version from PyPI:

```bash
python -m pip install nexo-os-info
```

To upgrade an existing installation:

```bash
python -m pip install --upgrade nexo-os-info
```

## Quick start

You can retrieve individual pieces of information directly:

```python
from nexo_os_info import (
    get_os_name,
    get_os_version,
    get_os_architecture,
    get_machine_name,
    get_python_version,
    get_processor,
    get_hostname,
)

print(get_os_name())
print(get_os_version())
print(get_os_architecture())
print(get_machine_name())
print(get_python_version())
print(get_processor())
print(get_hostname())
```

You can also retrieve common information together:

```python
from nexo_os_info import get_system_info

info = get_system_info()

for key, value in info.items():
    print(f"{key}: {value}")
```

Example output may look like:

```text
os: Windows
os_version: 10.0.26220
architecture: 64bit
machine: AMD64
python: 3.13.7
processor: Intel64 Family 6 Model 190
hostname: MY-PC
```

The exact values depend on the computer and operating system running your Python program.

## Available functions

### Operating system

`get_os_name()`  
Returns the operating-system name reported by Python.

`get_os_version()`  
Returns the current operating-system version reported by Python.

`get_os_architecture()`  
Returns the operating-system architecture, such as `32bit` or `64bit`.

### Computer information

`get_machine_name()`  
Returns the machine architecture identifier reported by Python.

`get_processor()`  
Returns processor information when it is available.

`get_hostname()`  
Returns the computer's hostname.

### Python information

`get_python_version()`  
Returns the Python version running the current program.

### Combined information

`get_system_info()`  
Returns a dictionary containing the common system-information values in one call.

The dictionary currently contains:

```text
os
os_version
architecture
machine
python
processor
hostname
```

### System uptime

`get_uptime()`  
Returns an uptime value when available.

> ℹ️ Uptime handling is still being developed and may receive platform-specific improvements in future versions.

## Operating-system detection

Nexo OS Info also provides simple helpers for checking the current operating system:

```python
from nexo_os_info import is_windows, is_linux, is_macos

if is_windows():
    print("Windows detected")

if is_linux():
    print("Linux detected")

if is_macos():
    print("macOS detected")
```

These helpers are useful when an application needs to choose platform-specific behavior without repeatedly writing the same checks.

## Designed to stay lightweight

Nexo OS Info is deliberately focused.

The project does **not** try to become a complete hardware-monitoring suite, task manager, benchmarking application, or system-management framework. Those are different jobs.

That means you can use Nexo OS Info when you only need basic information about the environment in which your Python application is running.

The project also keeps its test suite separate from the published library. Tests are used to improve reliability during development and CI, but they are not intended to become part of the runtime package.

## Reliability and safe fallbacks

System information is not always available in exactly the same way on every platform or environment. For that reason, the library uses safe fallbacks for several information functions.

When information cannot be retrieved, a function may return `"Unknown"` or, where appropriate, `None`.

This helps applications avoid unnecessary crashes simply because one piece of system information is unavailable.

## Development

Nexo OS Info is developed by **Nexo Studios**.

The project uses automated testing and GitHub Actions to build and publish releases. Development versions can contain changes that are not yet considered stable.

The project follows a versioned release process, with version 1.0.0 planned as the point where the public API is expected to become substantially more stable.

If you want to contribute, test a development version, report a problem, or suggest an improvement, use the project's GitHub repository.

## Feedback and contributions

Found a bug? Have an idea for a useful system-information function?

Contributions, bug reports, and practical suggestions are welcome. Before opening an issue, please check whether the problem has already been reported.

When reporting a bug, include useful information such as:

- Nexo OS Info version
- Python version
- operating system
- architecture
- the code that produced the problem
- the error message or traceback

This makes problems much easier to reproduce and fix.

## Project

**Nexo OS Info** is part of the Nexo Studios project ecosystem.

The project is built around a simple principle:

> **Useful information should be easy to access.**

If you are building a Python application that needs basic operating-system information, give Nexo OS Info a try.

---

**Nexo Studios — Building Tomorrow Together.**
