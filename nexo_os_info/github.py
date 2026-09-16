"""
GitHub Release and changelog utilities for Nexo OS Info.
"""

import json
import urllib.request
import urllib.error


GITHUB_API_URL = "https://api.github.com/repos/Nexo-Studios/nexo-os-info/releases"


def get_changelog():
    """
    Retrieve the changelog from GitHub Releases.

    Returns:
        str: A formatted changelog containing all published releases.
    """
    try:
        request = urllib.request.Request(
            GITHUB_API_URL,
            headers={
                "User-Agent": "Nexo-OS-Info"
            }
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            releases = json.loads(response.read().decode("utf-8"))

        if not releases:
            return "No releases found."

        changelog = []

        for release in releases:
            tag = release.get("tag_name", "Unknown version")
            name = release.get("name") or tag
            body = release.get("body") or "No changelog available."

            changelog.append(
                f"{name} ({tag})\n{body.strip()}"
            )

        return "\n\n".join(changelog)

    except urllib.error.URLError as error:
        return f"Unable to retrieve changelog: {error}"
    except (json.JSONDecodeError, ValueError):
        return "Unable to read GitHub release data."
