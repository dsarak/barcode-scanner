[app]

# (str) Title of your application
title = Barcode Scanner

# (str) Package name
package.name = barcodescanner

# (str) Package domain (needed for android/ios packaging)
package.domain = org.wireless.scanner

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec,pyc,pyo

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = bin, .buildozer, .git

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow,pyzbar,android

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = CAMERA,INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK API to use.
android.ndk_api = 21

# (list) The Android architectures to build for (e.g. armeabi-v7a, arm64-v8a)
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess downloads or save time
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only
android.accept_sdk_license = True

# (str) The entry point of your application
entrypoint = main.py

# (str) Android app theme
android.manifest.theme = @android:style/Theme.NoTitleBar.Fullscreen

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Android addition libraries to copy into libs/armeabi
# android.add_libs_arm64_v8a = libs/arm64-v8a/libzbar.so
# android.add_libs_armeabi_v7a = libs/armeabi-v7a/libzbar.so

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug when possible)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
