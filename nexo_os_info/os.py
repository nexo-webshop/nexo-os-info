import platform


def get_os_name():
    """Return the name of the current operating system."""
    try:
        os_name = platform.system()

        if not os_name:
            return "Unknown"

        return os_name

    except Exception:
        return "Unknown"
