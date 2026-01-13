[app]
title = Ung dung Python
version = 1.0

package.name = testapk
package.domain = org.demo

source.dir = .
source.include_exts = py

requirements = python3,kivy
android.permissions = INTERNET

# Quan trọng: chỉ rõ SDK cho GitHub Actions
android.sdk_path = /home/runner/android-sdk
