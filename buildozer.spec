[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

# Your app source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# Core requirements
requirements = python3,kivy

# App behaviour
orientation = portrait
fullscreen = 0

# Android targets
android.api = 33
android.minapi = 21
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a

# DO NOT SPECIFY SDK/NDK PATHS OR VERSIONS
# GitHub Actions installs the correct ones automatically

# Optional icons (uncomment if you use them)
# icon.filename = icon.png

# If using a splashscreen (optional)
# presplash.filename = presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

# Let python-for-android manage everything
# DO NOT override 'p4a.ndk_dir', 'p4a.sdk_dir' or 'android.ndk'
