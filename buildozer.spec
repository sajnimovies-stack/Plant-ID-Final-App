[app]
title = AI Plant Identifier
package.name = aiplantid
package.domain = org.naeem
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Professional Requirements
requirements = python3, kivy==2.3.0, kivymd==1.1.1, android, pyjnius, requests, certifi, urllib3

orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True
android.permissions = CAMERA, INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
