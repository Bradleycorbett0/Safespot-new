name: Build APK

on:
  workflow_dispatch:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Install System Dependencies
      run: |
        sudo apt update
        sudo apt install -y \
          git zip unzip openjdk-17-jdk python3 python3-pip python3-venv \
          libncurses6 libstdc++6 zlib1g-dev libffi-dev libssl-dev liblzma-dev
        pip install --upgrade pip

    - name: Create Python Virtual Env + Install Buildozer
      run: |
        python3 -m venv $HOME/venv
        source $HOME/venv/bin/activate
        pip install cython==0.29.36 buildozer==1.5.0

    - name: Configure Android SDK Paths
      run: |
        echo "ANDROIDSDK=/usr/local/lib/android/sdk" >> $GITHUB_ENV
        echo "ANDROID_HOME=/usr/local/lib/android/sdk" >> $GITHUB_ENV
        echo "ANDROID_SDK_ROOT=/usr/local/lib/android/sdk" >> $GITHUB_ENV
        echo "ANDROIDNDK=/usr/local/lib/android/sdk/ndk/23.1.7779620" >> $GITHUB_ENV
        echo "ANDROID_NDK_HOME=/usr/local/lib/android/sdk/ndk/23.1.7779620" >> $GITHUB_ENV
        echo "ANDROID_NDK_ROOT=/usr/local/lib/android/sdk/ndk/23.1.7779620" >> $GITHUB_ENV
        echo "JAVA_HOME=/usr/lib/jvm/temurin-17-jdk-amd64" >> $GITHUB_ENV
        echo "P4A_SKIP_NDK_INSTALL=1" >> $GITHUB_ENV

    - name: Build APK
      run: |
        source $HOME/venv/bin/activate

        # Remove conflicting Android variables
        unset ANDROIDSDK
        unset ANDROID_HOME
        unset ANDROID_SDK_ROOT
        unset ANDROID_NDK_HOME
        unset ANDROID_NDK
        unset ANDROIDNDK_HOME

        # Re-export correct Android values
        export ANDROIDSDK=/usr/local/lib/android/sdk
        export ANDROID_HOME=/usr/local/lib/android/sdk
        export ANDROID_SDK_ROOT=/usr/local/lib/android/sdk
        export ANDROIDNDK=$ANDROIDSDK/ndk/23.1.7779620
        export ANDROID_NDK_HOME=$ANDROIDNDK
        export ANDROID_NDK=$ANDROIDNDK
        export ANDROIDNDK_HOME=$ANDROIDNDK
        export JAVA_HOME=/usr/lib/jvm/temurin-17-jdk-amd64
        export P4A_SKIP_NDK_INSTALL=1
        export P4A_RELEASE_BUILD=1

        echo "Using SDK: $ANDROIDSDK"
        echo "Using NDK: $ANDROIDNDK"
        echo "Using JAVA: $JAVA_HOME"

        # 🔥 CRITICAL — pin python-for-android to NDK 23 compatible version
        sed -i 's|git clone -b master|git clone -b v2023.10.16|' $(which buildozer)

        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: safespot-apk
        path: bin/*.apk
