# Android Barcode Scanner App (Kivy / Buildozer)

This folder contains the complete source code and configuration for building the Android wireless scanner gun application.

---

## 📱 Features

- **Full-Screen Camera Preview**: Real-time camera feed utilizing hardware acceleration.
- **Center Targeting Reticle**: Custom graphics overlay with corner brackets and an animated red laser scanning line.
- **2D & 1D Barcode Support**: Decodes QR Codes, EAN-13, UPC-A, Code 128, Code 39, Interleaved 2 of 5, etc. via `pyzbar`.
- **Intelligent Debounce Timer**: 2.5-second lockout for duplicate barcodes with on-screen cooldown countdown.
- **Visual & Haptic Feedback**: Flash-green animation on target reticle and 60ms phone vibration on successful decode.
- **Non-blocking TCP Socket**: Dedicated worker thread and queue transmitting `{"type": "...", "data": "..."}\n` without dropping UI frames.
- **Runtime Permissions**: Requests Android `CAMERA` and `INTERNET` permissions upon startup.

---

## 🛠️ Building the .apk

Building Android packages requires a Linux environment (Ubuntu 20.04/22.04 LTS, WSL2 on Windows, or GitHub Actions).

### Method 1: Local Build (Ubuntu or WSL2)

#### 1. Install System Dependencies
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev libzbar0 libzbar-dev
```

#### 2. Install Buildozer and Cython
```bash
pip3 install --user --upgrade buildozer cython virtualenv
```

#### 3. Build Debug APK
Navigate to this folder and run:
```bash
cd android_scanner
buildozer android debug
```
The compiled APK will be generated in:
`bin/barcodescanner-1.0.0-arm64-v8a_armeabi-v7a-debug.apk`

#### 4. Deploy Directly to Phone via USB
Enable **USB Debugging** on your Android phone, connect it via USB, and run:
```bash
buildozer android debug deploy run logcat
```

---

## ☁️ Method 2: Free Cloud Build with GitHub Actions (No Linux/WSL needed!)

If you are on Windows and don't want to install WSL2 or hundreds of megabytes of Android SDKs, you can use GitHub Actions to build your APK automatically in the cloud.

A preconfigured GitHub Actions workflow is provided in:
`.github/workflows/build_apk.yml`

1. Push your repository to GitHub.
2. Go to the **Actions** tab on your GitHub repository.
3. The workflow builds the APK and lets you download the compiled `.apk` directly from the workflow artifacts!

---

## ⚙️ Understanding `pyzbar` & Native `libzbar` on Android

- `pyzbar` is a Python ctypes wrapper around the C library `libzbar.so`.
- When building on Android via Buildozer, `python-for-android` compiles C extensions.
- If your buildozer recipe requires native precompiled `libzbar.so` libraries for `arm64-v8a` and `armeabi-v7a`, you can place them into:
  - `libs/arm64-v8a/libzbar.so`
  - `libs/armeabi-v7a/libzbar.so`
  and uncomment the corresponding lines in `buildozer.spec`:
  ```ini
  android.add_libs_arm64_v8a = libs/arm64-v8a/libzbar.so
  android.add_libs_armeabi_v7a = libs/armeabi-v7a/libzbar.so
  ```

---

## 🚀 Running on Mobile

1. Open the app on your phone.
2. Grant camera permissions when prompted.
3. Ensure your phone is connected to the **same Wi-Fi network** as your Windows PC.
4. In the top bar, enter the **IP address** shown on your Windows PC screen (e.g., `192.168.1.100`) and port `5000`.
5. Tap **Connect**. The status indicator will switch to green.
6. Aim your phone at any barcode or QR code. The laser will scan it, flash green, vibrate, and beam the data directly into your active PC window!
