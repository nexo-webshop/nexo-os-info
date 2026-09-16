"""
GitHub Release and changelog utilities for Nexo OS Info.
"""

import json
import urllib.error
import urllib.request


GITHUB_API_URL = (
    "https://api.github.com/repos/Nexo-Studios/nexo-os-info/releases"
)


def get_changelog():
    """
    Retrieve the changelog from GitHub Releases.

    Returns:
        str: A formatted changelog.
    """
    try:
        request = urllib.request.Request(
            GITHUB_API_URL,
            headers={
                "User-Agent": "Nexo-OS-Info"
            },
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            releases = json.loads(
                response.read().decode("utf-8")
            )

        if not isinstance(releases, list):
            return "Unable to read GitHub release data."

        if not releases:
            return "No releases found."

        changelog = []

        for release in releases:
            if not isinstance(release, dict):
                continue

            tag = release.get("tag_name") or "Unknown version"
            name = release.get("name") or tag
            body = release.get("body") or "No changelog available."

            changelog.append(
                f"{name} ({tag})\n{body.strip()}"
            )

        if not changelog:
            return "No valid releases found."

        return "\n\n".join(changelog)

    except urllib.error.HTTPError as error:
        return f"Unable to retrieve changelog: HTTP {error.code}"

    except urllib.error.URLError:
        return "Unable to retrieve changelog."

    except TimeoutError:
        return "Unable to retrieve changelog: request timed out."

    except (json.JSONDecodeError, ValueError):
        return "Unable to read GitHub release data."

    except Exception:
        return "Unable to retrieve changelog."
