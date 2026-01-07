[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.ndk = 25b
android.accept_sdk_license = True

# 🔴 THESE TWO LINES ARE CRITICAL
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
