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

# In lines ko ya toh khali chor dein ya delete kar dein
android.sdk = 
android.ndk = 

android.accept_sdk_license = True
android.archs = arm64-v8a

# IS LINE KO DELETE KAR DEIN YA AISE LIKHEIN:
p4a.branch = master
