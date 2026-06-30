#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST_DIR="$ROOT_DIR/dist"
BUILD_DIR="$ROOT_DIR/build"
STAGING_DIR="$ROOT_DIR/dmg-staging"
APP_NAME="FlappyBird"
APP_BUNDLE="$DIST_DIR/$APP_NAME.app"
DMG_PATH="$DIST_DIR/${APP_NAME}-macOS.dmg"

cd "$ROOT_DIR"

python3 -m PyInstaller \
  --noconfirm \
  --clean \
  --windowed \
  --onedir \
  --name "$APP_NAME" \
  --osx-bundle-identifier "com.quentin.flappybird" \
  --add-data "bird.png:." \
  --add-data "pipe.png:." \
  play.py

rm -rf "$STAGING_DIR"
mkdir -p "$STAGING_DIR"
cp -R "$APP_BUNDLE" "$STAGING_DIR/"
ln -s /Applications "$STAGING_DIR/Applications"

rm -f "$DMG_PATH"
hdiutil create \
  -volname "$APP_NAME" \
  -srcfolder "$STAGING_DIR" \
  -ov \
  -format UDZO \
  "$DMG_PATH"

rm -rf "$STAGING_DIR"

echo "Application generee : $APP_BUNDLE"
echo "DMG genere : $DMG_PATH"
