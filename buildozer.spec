[app]
title = SafeSpot
package.name = safespot
package.domain = org.safespot

version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,json

requirements = python3,kivy

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# CRITICAL: Force CI paths (prevents NDK download crash)
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-ndk

log_level = 2


[android]
android.api = 33
android.minapi = 21
android.ndk = 25c

p4a.branch = master
p4a.bootstrap = sdl2

gradle_dependencies =
android.enable_androidx = True
android.enable_jetifier = True

# DO NOT SET android.sdk or android.ndk here (deprecated)


[buildozer]
warn_on_root = 0
