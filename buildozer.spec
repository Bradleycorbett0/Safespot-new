[app]

title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones.safespot
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy,openssl,android

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk_api = 21      # 🔥 REQUIRED TO STOP NDK DOWNLOAD
android.build_tools_version = 33.0.2

android.archs = armeabi-v7a, arm64-v8a

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/23.1.7779620
android.ndk = 23.1.7779620

android.accept_sdk_license = True
android.skip_update = True

# 🔥 ENSURES NO DOWNLOAD FROM P4A
p4a.no_download = True
p4a.local_recipes = .

android.gradle_version = 7.5
android.allow_backup = True

android.debug_artifact = apk
android.release_artifact = aab


[buildozer]
log_level = 2
warn_on_root = 1
