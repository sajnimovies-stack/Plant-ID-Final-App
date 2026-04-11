[app]
title = Plant Scanner Pro
package.name = plantscanner
package.domain = org.test
source.dir = .
requirements = python3, kivy==2.3.0, kivymd==1.1.1, camera4kivy, gestures4kivy, requests, certifi, pillow

# Android Specific
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True
android.grant_runtime_permissions = True

# Permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Ye line naye camera ke liye zaroori hai
android.meta_data = androidx.core.content.FileProvider
