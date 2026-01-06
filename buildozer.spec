[app]
title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,otf,wav,mp3

requirements = python3,kivy,requests,urllib3,idna,certifi,charset-normalizer

orientation = portrait
fullscreen = 0

# CRITICAL: show real errors
log_level = 2


[buildozer]
warn_on_root = 1


[android]
bootstrap = sdl2

# API levels
api = 33
minapi = 21
ndk_api = 21

# Architectures
# NOTE: armeabi-v7a is increasingly fragile on Ubuntu 24 runners.
# You can re-add it later once arm64 builds cleanly.
arch = arm64-v8a

# THIS IS THE FIX — correct keys
android.sdk_path = android-sdk

# Let Buildozer use its supported NDK, but keep it consistent
ndk_version = 25b

accept_sdk_license = True

permissions = INTERNET

android.enable_androidx = True
