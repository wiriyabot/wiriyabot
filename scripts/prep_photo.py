"""Prepare a portrait photo for ASCII conversion.

    python scripts/prep_photo.py .local/source-photo.jpg

Crops to head and shoulders, pushes the (already light) background to pure
white, and boosts local contrast with CLAHE so facial features survive the
coarse character grid. Writes .local/source-prepped.png (grayscale).
"""
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".local" / "source-prepped.png"

# Crop box as fractions of the source image (left, top, right, bottom).
CROP = (0.1, 0.04, 0.9, 0.86)
BG_THRESHOLD = 232


def background_mask(gray):
    """Light pixels connected to the image border = background."""
    light = (gray >= BG_THRESHOLD).astype(np.uint8)
    h, w = light.shape
    mask = np.zeros((h + 2, w + 2), np.uint8)
    for x, y in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0)):
        if light[y, x]:
            cv2.floodFill(light, mask, (x, y), 2)
    bg = (light == 2).astype(np.uint8)
    # Close small gaps along hair edges so the outline stays clean.
    return cv2.morphologyEx(bg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)).astype(bool)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / ".local" / "source-photo.jpg")
    img = cv2.imdecode(np.fromfile(src, np.uint8), cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    l, t, r, b = CROP
    img = img[int(t * h):int(b * h), int(l * w):int(r * w)]

    bg = background_mask(img)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    out = clahe.apply(img)
    out[bg] = 255

    OUT.parent.mkdir(exist_ok=True)
    cv2.imencode(".png", out)[1].tofile(str(OUT))
    print(f"wrote {OUT} {out.shape[1]}x{out.shape[0]}, background {bg.mean():.0%}")


if __name__ == "__main__":
    main()
