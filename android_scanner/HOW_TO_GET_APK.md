# 📱 How to Get Your Android APK File

The **Windows PC Receiver (`dist/BarcodeReceiver.exe`)** is already compiled and ready to use on your PC.

The **Android APK (`.apk`)** has **not been compiled yet** because **Buildozer** (the Kivy Android packaging engine) requires a **Linux** environment. Native Windows cannot compile Android APKs directly with Buildozer.

You have **3 simple ways** to get your `.apk` file:

---

## ⚡ Method 1: Google Colab (Recommended — Free, 100% in Browser, No Setup)

Google Colab gives you a free Linux machine in your browser. You can build and download your `.apk` in ~10 minutes.

### Steps:
1. Go to [Google Colab](https://colab.research.google.com/) and click **"New notebook"**.
2. On the left sidebar, click the **Folder icon (Files)**.
3. Drag and drop the **`android_scanner.zip`** file (already prepared in this project folder) into the Colab file area.
4. Copy and paste the following block into a code cell and click **Run (Play button)**:

```python
# 1. Unzip the project
!unzip -o android_scanner.zip -d app

# 2. Install Buildozer and system dependencies
!sudo apt update
!sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev libzbar0 libzbar-dev
!pip install --upgrade buildozer cython virtualenv

# 3. Build the APK
!cd app && buildozer android debug

# 4. Automatically download the APK to your computer
from google.colab import files
import glob

apks = glob.glob("app/bin/*.apk")
if apks:
    print(f"Build complete! Downloading {apks[0]}...")
    files.download(apks[0])
else:
    print("Error: APK not found in app/bin/")
```

5. When the build finishes, your browser will automatically prompt you to save the `.apk` file!
6. Transfer the `.apk` to your Android phone via USB, Google Drive, or WhatsApp, tap to install, and you're ready to scan!

---

## ☁️ Method 2: GitHub Actions (Free Automated Cloud Build)

If you use GitHub, a preconfigured workflow is already included in this repository:
[`.github/workflows/build_apk.yml`](../.github/workflows/build_apk.yml)

### Steps:
1. Initialize git and push this project to a new repository on GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
2. Open your repository on GitHub in your web browser.
3. Click the **"Actions"** tab at the top.
4. Click on the running **"Build Android APK"** workflow.
5. Once completed (green checkmark), look at the bottom under **"Artifacts"** and click **`BarcodeScanner-APK`** to download your compiled `.apk`.

---

## 💻 Method 3: Windows Subsystem for Linux (WSL2)

If you prefer building locally on your Windows machine:

1. Open PowerShell as Administrator and install WSL:
   ```powershell
   wsl --install
   ```
2. Restart your computer and open Ubuntu from your Start menu.
3. Run:
   ```bash
   sudo apt update
   sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev libzbar0 libzbar-dev
   pip3 install --user --upgrade buildozer cython virtualenv
   cd "/mnt/c/Users/wilso/OneDrive/Desktop/Web Video/Barcode Scanner/android_scanner"
   buildozer android debug
   ```
4. The `.apk` will be output to `android_scanner/bin/barcodescanner-1.0.0-arm64-v8a_armeabi-v7a-debug.apk`.
