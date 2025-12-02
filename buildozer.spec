[app]

title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# Requirements
requirements = python3,kivy,openssl,android

orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Android configuration
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

# Architectures
android.archs = armeabi-v7a, arm64-v8a

# Paths for GitHub runner
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.0.8775105
android.ndk = 25.0.8775105

# No SDK downloads
android.accept_sdk_license = True
android.skip_update = True

# Gradle
android.gradle_version = 7.5
android.allow_backup = True

# Artifacts
android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1
