[app]
title = Plant Identifier
package.name = plantidapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requirements ko simplify kiya hai taake conflict na ho
requirements = python3, kivy==2.3.0, kivymd==1.1.1, requests, certifi, pillow

orientation = portrait
fullscreen = 0

# Android specific settings (Pixel 6 Fixes)
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True

# Permissions (Professional apps ke liye zaroori)
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Naye Android versions (14/15) ke liye ye settings lazmi hain
android.enable_androidx = True
android.grant_runtime_permissions = True
android.accept_sdk_license = True

# P4A settings
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
