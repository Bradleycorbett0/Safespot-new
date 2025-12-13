[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones

version = 1.0

source.dir = .
source.include_exts = py,kv,png,jpg,json,txt,atlas

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

# ---------- ANDROID ----------
android.api = 33
android.minapi = 21

# IMPORTANT: use NDK 25b (stable with p4a)
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET

# Auto-accept licenses
android.accept_sdk_license = True

# ---------- BUILD ----------
[buildozer]
log_level = 2
warn_on_root = 1
