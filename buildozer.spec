[app]

title = SafeSpot
package.name = safespot
package.domain = com.bradleycorbettjones

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,txt

source.include_patterns = assets/*,assets/*.png,assets/*.jpg,assets/*.jpeg,screens/*,screens/*.py

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.archs = arm64-v8a, armeabi-v7a

presplash.filename = assets/safespot_logo.png
icon.filename = assets/safespot_logo.png

log_level = 2

warn_on_root = 0

osx.python_version = 3
osx.kivy_version = 2.3.0

p4a.branch = master

android.gradle_dependencies =

android.enable_androidx = True

android.add_packaging_options = META-INF/*.kotlin_module

[buildozer]

log_level = 2

warn_on_root = 0
