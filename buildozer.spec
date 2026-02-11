[app]

# (str) Title of your application
title = SafeSpot

# (str) Package name
package.name = safespot

# (str) Package domain (must match your Firebase setup)
package.domain = com.bradleycorbettjones

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg,jpeg,atlas,json

# (str) Application version
version = 1.0

# (list) Requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# ==================================================
# ANDROID SETTINGS (CRITICAL SECTION)
# ==================================================

# Target API
android.api = 33

# Minimum supported API
android.minapi = 21

# Force NDK version (fixes NoneType error)
android.ndk = 25b

# NDK API
android.ndk_api = 21

# Force compatible Build Tools
android.sdk_build_tools_version = 33.0.2

# Permissions (adjust if needed later)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# AndroidX support
android.enable_androidx = True

# ==================================================
# BUILD OPTIONS
# ==================================================

# (bool) Use logcat
logcat_filters = *:S python:D

# (bool) Warn on Python 2 syntax
warn_on_root = 1


# ==================================================
# DEBUG / RELEASE
# ==================================================

# Uncomment for release builds later
# android.release_artifact = aab
# android.debug_artifact = apk
