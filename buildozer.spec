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

android.api = 33
android.minapi = 21

android.permissions = INTERNET

android.archs = arm64-v8a, armeabi-v7a

# CRITICAL — STOP BUILD-TOOLS DRIFT
android.sdk = 33
android.build_tools_version = 33.0.2
android.ndk = 25.2.9519653

# CRITICAL — DISABLE INTERNAL SDK DOWNLOADS
android.skip_update = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
