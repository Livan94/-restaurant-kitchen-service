from restaurant_kitchen_service.settings.base import *  # noqa: F403,F401

# Debug Toolbar
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE = (["debug_toolbar.middleware.DebugToolbarMiddleware"]
              + MIDDLEWARE)  # noqa: F405

INTERNAL_IPS = [
    "127.0.0.1",
]


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}
