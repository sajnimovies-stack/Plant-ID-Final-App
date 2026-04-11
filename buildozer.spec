[app]
title = Plant Identifier
package.name = plantidapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Requirements mein latest stable versions rakhein
requirements = python3, kivy==2.3.0, kivymd==1.1.1, requests, certifi, pillow

# Android versions for Pixel 6 (API 33 is best)
android.api = 33
android.minapi = 24
android.ndk = 25b

# Pixel 6 (arm64-v8a) support
android.archs = arm64-v8a

# Stability Fixes (Naye phones ke liye)
android.enable_androidx = True
android.grant_runtime_permissions = True

# NDK version ko lazmi specify karein taake crash na ho
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Is line ko master par hi rehne dein ya delete kar dein
p4a.branch = master
