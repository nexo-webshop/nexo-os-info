"""
Nexo OS Info
A simple Python package for retrieving operating system information
and GitHub release changelogs.
"""

from .os import get_os_name
from .github import get_changelog

__version__ = "0.0.1.4"

__all__ = [
    "get_os_name",
    "get_changelog",
]
