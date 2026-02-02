[app]
title = ContoUP
package.name = contoup
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait
android.permissions = NFC, INTERNET
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
