[app]

# =========================
# Application Information
# =========================

title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,ttf,otf

version = 0.1

# =========================
# Python & Kivy
# =========================

requirements = python3,kivy
entrypoint = main.py

# =========================
# Android Configuration
# =========================

# API levels
android.api = 33
android.minapi = 21

# NDK (p4a recommended)
android.ndk = 25b

# SDK (do NOT set sdk_path)
android.sdk = 33

# Build tools (stable + supported)
android.build_tools_version = 33.0.2

# Accept licenses automatically
android.accept_sdk_license = True

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Bootstrap (required)
p4a.bootstrap = sdl2

# =========================
# Permissions
# =========================

android.permissions = INTERNET

# =========================
# App Behavior
# =========================

android.allow_backup = True
android.orientation = portrait

# =========================
# Logging / Debug
# =========================

android.logcat_filters = *:S python:D
android.debuggable = 1

# =========================
# Build Optimization
# =========================

android.private_storage = True
android.enable_androidx = True

# =========================
# Exclusions
# =========================

exclude_exts = spec,pyc,pyo,swp,log
