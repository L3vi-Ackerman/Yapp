from core.settings._defaults import Defaults as D


class AppsSettings:
    INSTALLED_APPS = D.INSTALLED_APPS + [
        "gatekeeper",
        "_user",
        "chat",
        "message",
        "membership",
        "room",
        "health",
    ]
