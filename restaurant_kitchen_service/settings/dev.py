from restaurant_kitchen_service.settings.base import *  # noqa: F403,F401

# Debug Toolbar
DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE = (["debug_toolbar.middleware.DebugToolbarMiddleware"]
              + MIDDLEWARE)  # noqa: F405

INTERNAL_IPS = [
    "127.0.0.1",
]
