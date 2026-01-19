name: Tao APK Python

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - uses: actions/checkout@v4

      - name: Setup Java 17
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Setup Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install system dependencies
        run: |
          sudo apt update
          sudo apt install -y \
            git zip unzip \
            autoconf automake libtool \
            pkg-config build-essential \
            cmake

      - name: Install Python packages
        run: |
          pip install --upgrade pip
          pip install cython buildozer kivy

      - name: Install Android SDK & NDK
        run: |
          ANDROID_SDK_ROOT=$HOME/android-sdk
          mkdir -p $ANDROID_SDK_ROOT/cmdline-tools
          cd $ANDROID_SDK_ROOT/cmdline-tools

          wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
          unzip commandlinetools-linux-11076708_latest.zip
          mv cmdline-tools latest
          rm commandlinetools-linux-11076708_latest.zip

          export PATH=$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$PATH

          yes | sdkmanager --licenses

          sdkmanager \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2" \
            "ndk;23.2.8568313"

      - name: Build APK
        env:
          ANDROID_SDK_ROOT: ${{ runner.home }}/android-sdk
          ANDROID_HOME: ${{ runner.home }}/android-sdk
          ANDROID_NDK_HOME: ${{ runner.home }}/android-sdk/ndk/23.2.8568313
          PATH: ${{ runner.home }}/android-sdk/cmdline-tools/latest/bin:${{ env.PATH }}
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: apk
          path: bin/*.apk
