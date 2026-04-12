[app]
title = AI Plant Identifier
package.name = aiplantid
package.domain = org.naeem
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Professional Requirements (Pyjnius is must for Gallery/Camera)
requirements = python3, kivy==2.3.0, kivymd==1.1.1, android, pyjnius, requests, certifi, urllib3

orientation = portrait
fullscreen = 0

# Android Settings (Targeting Android 14)
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True
android.grant_runtime_permissions = True
android.accept_sdk_license = True

# Permissions (Android 14 Scoped Storage included)
android.permissions = CAMERA, INTERNET, READ_MEDIA_IMAGES, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Metadata for FileProvider
android.meta_data = androidx.core.content.FileProvider=org.naeem.aiplantid.fileprovider

# Build settings
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
