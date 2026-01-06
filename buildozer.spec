[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,otf,wav,mp3

# Keep requirements minimal and stable
requirements = python3,kivy,requests,urllib3,idna,certifi,charset-normalizer

orientation = portrait
fullscreen = 0

# Show real errors
log_level = 2


[buildozer]
warn_on_root = 1


[android]
# Correct bootstrap
bootstrap = sdl2

# Android API levels
api = 33
minapi = 21
ndk_api = 21

# Architectures
# arm64 is the most reliable on modern runners
arch = arm64-v8a

# CRITICAL: correct, recognised keys
android.sdk_path = android-sdk

# Let Buildozer manage a compatible NDK
ndk_version = 25b

# Required for CI
accept_sdk_license = True

# Permissions
permissions = INTERNET

# AndroidX support
android.enable_androidx = True
