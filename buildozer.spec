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

# ---- ANDROID CONFIG ----
android.api = 33
android.minapi = 21
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a

# Force correct build tools & NDK
android.build_tools_version = 33.0.2
android.ndk = 25b
android.accept_sdk_license = True
android.allow_downloads = True

# Do NOT hardcode paths (GitHub runner varies)
# These lines were removed:
# android.sdk_path =
# android.ndk_path =

[buildozer]
log_level = 2
warn_on_root = 1

# python-for-android integration
p4a.branch = master
# Remove path overrides so p4a installs correctly
# p4a.sdk_dir =
# p4a.ndk_dir =
# p4a.dir =
