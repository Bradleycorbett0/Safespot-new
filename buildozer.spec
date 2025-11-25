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

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

android.archs = armeabi-v7a, arm64-v8a

android.sdk_path = $ANDROIDSDK
android.ndk_path = $ANDROIDNDK
android.ndk = 25b

android.gradle_version = 7.5
android.allow_backup = True

android.release_artifact = aab
android.debug_artifact = apk


[buildozer]
log_level = 2
warn_on_root = 1
