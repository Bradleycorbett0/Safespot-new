[app]

title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# Python/Kivy stack for Android build
requirements = python3,kivy,android,openssl

orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Android versions
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# Architectures
android.archs = armeabi-v7a, arm64-v8a

#
# SDK / NDK CONFIGURATION
# ============================================================
#
# IMPORTANT: Do NOT use $ANDROIDSDK or $ANDROIDNDK here
# These must be absolute paths so Buildozer does NOT download anything
#

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/23.1.7779620
android.ndk = 23.1.7779620
android.accept_sdk_license = True

#
# Gradle & artifacts
#
android.gradle_version = 7.5
android.allow_backup = True

# Debug produces APK, Release produces AAB for Play Store
android.release_artifact = aab
android.debug_artifact = apk


[buildozer]
# Verbosity for debugging
log_level = 2
warn_on_root = 1
