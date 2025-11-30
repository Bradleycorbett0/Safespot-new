[app]

# App details
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# App requirements
# android + openssl are required for Kivy apps on Android
requirements = python3,kivy,android,openssl

# Orientation
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Android build config
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# CPU architectures
android.archs = armeabi-v7a, arm64-v8a

#
# ---- ANDROID PATH CONFIGURATION (DO NOT CHANGE) ----
# These MUST be absolute paths and MUST match the GitHub workflow
#

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/23.1.7779620
android.ndk = 23.1.7779620

# Prevent Buildozer / p4a from downloading SDK components
android.accept_sdk_license = True
android.skip_update = True

# Gradle & artifacts
android.gradle_version = 7.5
android.allow_backup = True

# Debug produces an apk, release produces an aab for Play Store
android.debug_artifact = apk
android.release_artifact = aab


[buildozer]
log_level = 2
warn_on_root = 1
