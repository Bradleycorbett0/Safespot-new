[app]

title = SafeSpot

package.name = safespot
package.domain = com.bradleycorbettjones

source.dir = .

source.include_exts = py,kv,png,jpg,jpeg,json,txt,atlas
source.include_patterns = *.py,*.json,*.png,*.jpg,*.jpeg,assets/*

version = 1.0

requirements = python3,kivy==2.2.1,requests

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

android.sdk_build_tools_version = 33.0.2

android.accept_sdk_license = True

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA

android.archs = arm64-v8a,armeabi-v7a

android.enable_androidx = True

p4a.branch = v2024.01.21

log_level = 2

warn_on_root = 0


[buildozer]

log_level = 2

warn_on_root = 0
