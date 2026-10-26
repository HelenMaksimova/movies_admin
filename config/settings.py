from split_settings.tools import include

# Base project settings
include("components/base_settings.py")


# Application definition
include("components/app_definition.py")


# Database
include("components/database.py")


# Password validation
include("components/pswd_validation.py")


# Internationalization
include("components/internationalization.py")


# Logging
include("components/log_settings.py")
