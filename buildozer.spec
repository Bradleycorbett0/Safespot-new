[app]

# (str) Title of your application
title = SafeSpot

# (str) Package name
package.name = safespot

# (str) Package domain (use your real domain or github user)
package.domain = com.bradleycorbettjones

# (str) Source code where the main.py lives
source.dir = .

# (str) The entry point of the application
source.main = main.py

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0


# -------------------------------
# ANDROID CONFIGURATION
# -------------------------------

# (list) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API
android.api = 33

# (int) Minimum Android API
android.minapi = 21

# (str) REQUIRED: python-for-android compatible NDK
android.ndk = 25b

# (str) Android SDK version (leave empty – Buildozer handles this)
android.sdk =

# (bool) Allow backup
android.allow_backup = True

# (bool) Use SDL2 bootstrap
android.bootstrap = sdl2

# (bool) Enable debug symbols (debug builds only)
android.debug = True


# -------------------------------
# PERMISSIONS
# -------------------------------

android.permissions = INTERNET, ACCESS_NETWORK_STATE


# -------------------------------
# PYTHON FOR ANDROID
# -------------------------------

# (str) Python version
p4a.python_version = 3.10

# (bool) Copy libraries into APK
p4a.copy_libs = True

# (bool) Ignore setup.py
p4a.ignore_setup_py = True

# (bool) Use colors in logs
p4a.color = always


# -------------------------------
# BUILD OPTIONS
# -------------------------------

# (int) Log level (2 = very verbose, helpful for CI)
log_level = 2

# (bool) Clean build before compiling
clean = False

# (bool) Warning on deprecated APIs
warn_on_root = False


# -------------------------------
# DO NOT SET THESE (IMPORTANT)
# -------------------------------
# android.sdk_path
# android.ndk_path
# p4a.sdk_dir
# p4a.ndk_dir
# p4a.build_dir
# p4a.dist_dir
