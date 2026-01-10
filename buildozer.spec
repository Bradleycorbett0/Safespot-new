[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Entry point (adjust if your main file differs)
entrypoint = main.py

# Android configuration
android.api = 33
android.minapi = 21
android.ndk_api = 21

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a

# Disable deprecated / problematic options
android.sdk = 
android.ndk = 
android.sdk_path =
android.ndk_path =

# Logging
log_level = 2

# Fix for modern toolchains
android.allow_backup = True
android.accept_sdk_license = True

# Gradle (recommended defaults)
android.gradle_dependencies =
android.enable_androidx = True

# Packaging
android.private_storage = True
android.release_artifact = apk

# Keep build directories between runs
presplash.filename =
icon.filename =

[buildozer]
warn_on_root = 1
log_level = 2
