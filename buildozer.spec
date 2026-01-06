name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-24.04

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y \
          python3 \
          python3-pip \
          python3-venv \
          openjdk-17-jdk \
          unzip \
          zip \
          git \
          build-essential \
          libffi-dev \
          libssl-dev \
          libsqlite3-dev \
          zlib1g-dev \
          liblzma-dev \
          libncurses6

    - name: Set up Python virtual environment
      run: |
        python3 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install buildozer cython

    - name: Download Android SDK
      run: |
        mkdir -p android-sdk/cmdline-tools
        cd android-sdk/cmdline-tools
        wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
        unzip commandlinetools-linux-*.zip
        mv cmdline-tools latest

    - name: Set Android environment variables
      run: |
        echo "ANDROID_SDK_ROOT=$GITHUB_WORKSPACE/android-sdk" >> $GITHUB_ENV
        echo "ANDROID_HOME=$GITHUB_WORKSPACE/android-sdk" >> $GITHUB_ENV
        echo "ANDROIDSDK=$GITHUB_WORKSPACE/android-sdk" >> $GITHUB_ENV
        echo "$GITHUB_WORKSPACE/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH
        echo "$GITHUB_WORKSPACE/android-sdk/platform-tools" >> $GITHUB_PATH

    - name: Accept Android licenses
      run: |
        yes | sdkmanager --licenses

    - name: Install Android SDK components
      run: |
        sdkmanager \
          "platform-tools" \
          "platforms;android-33" \
          "build-tools;33.0.2" \
          "ndk;25.2.9519653" \
          "cmake;3.22.1"

    - name: Build APK with Buildozer
      run: |
        source venv/bin/activate
        buildozer android debug

    - name: Upload APK artifact
      uses: actions/upload-artifact@v4
      with:
        name: SafeSpot-APK
        path: bin/*.apk
