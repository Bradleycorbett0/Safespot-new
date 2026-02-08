[app]
title = SafeSpot
package.name = safespot
package.domain = org.safespot

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

# ANDROID SETTINGS
android.api = 33
android.minapi = 21

# 🔴 REQUIRED — fixes the NoneType / group crash
android.ndk = 25b
android.ndk_api = 21

android.permissions = INTERNET
android.allow_backup = True

# DO NOT SET android.sdk (deprecated)
# android.sdk = 33 ❌ REMOVE

# ARCHITECTURES
android.archs = arm64-v8a,armeabi-v7a

# LOGGING
log_level = 2

[buildozer]
warn_on_root = 1
