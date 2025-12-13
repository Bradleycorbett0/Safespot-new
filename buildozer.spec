[app]
title = SafeSpot
package.name = safespot
package.domain = bradleycorbettjones
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android configuration
android.api = 33
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET
android.build_tools_version = 33.0.2

# Use SDL2 bootstrap (recommended)
android.bootstrap = sdl2

# Keep logs readable
log_level = 2


[buildozer]
warn_on_root = 1
log_level = 2
