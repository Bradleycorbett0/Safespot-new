[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a
android.build_tools_version = 33.0.2

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/23.1.7779620
android.ndk = 23.1.7779620

[buildozer]
log_level = 2
warn_on_root = 1

p4a.sdk_dir = /usr/local/lib/android/sdk
p4a.ndk_dir = /usr/local/lib/android/sdk/ndk/23.1.7779620
p4a.dir = /home/runner/.buildozer/android/platform/python-for-android
