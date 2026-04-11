[app]
title = Plant Identifier
package.name = plantidapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,certifi
orientation = portrait
fullscreen = 0
android.permissions = CAMERA, INTERNET
android.api = 33
android.minapi = 21

# NDK version ko lazmi specify karein taake crash na ho
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Is line ko master par hi rehne dein ya delete kar dein
p4a.branch = master
