[app]
title = Plant Scanner Pro
package.name = plantscanner
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requirements
requirements = python3, kivy==2.3.0, kivymd==1.1.1, camera4kivy, gestures4kivy, requests, certifi, pillow

orientation = portrait
fullscreen = 0

# Android Settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True
android.grant_runtime_permissions = True
android.accept_sdk_license = True

# Permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android Specific Fixes
android.meta_data = androidx.core.content.FileProvider=org.test.plantscanner.fileprovider

# Build settings
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
