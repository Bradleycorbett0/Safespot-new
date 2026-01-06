[app]

title = SafeSpot
package.name = safespot
package.domain = org.safespot

source.dir = .
source.main = main.py

version = 0.1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 33
android.sdk = 33
android.ndk = 25.2.9519653
android.ndk_api = 21
android.build_tools_version = 33.0.2

android.archs = arm64-v8a
android.permissions = INTERNET

android.enable_androidx = True
android.allow_backup = True
android.copy_libs = True
android.use_legacy_toolchain = False
