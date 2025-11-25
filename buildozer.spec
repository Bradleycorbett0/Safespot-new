[app]

# App details
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# Dependencies
requirements = python3,kivy

# Display
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Android API + build tools
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# Architectures
android.archs = armeabi-v7a, arm64-v8a

# -------------------------------
# IMPORTANT FOR GITHUB BUILDS
# -------------------------------
android.sdk_path = $ANDROIDSDK
android.ndk_path = $ANDROIDNDK
android.ndk = 25b

# Gradle / Java
android.gradle_version = 7.5

# Backup support
android.allow_backup = True

# Build outputs
android.release_artifact = aab
android.debug_artifact = apk


[buildozer]
log_level = 2
warn_on_root = 1
