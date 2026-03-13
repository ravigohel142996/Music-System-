"""
helpers.py
Miscellaneous utility functions used across the application.
"""

import base64
import io
import os
from typing import Optional, Tuple

import numpy as np
from PIL import Image


def pil_to_base64(image: Image.Image, fmt: str = "PNG") -> str:
    """
    Convert a PIL Image to a base64-encoded string.

    Args:
        image: PIL Image object.
        fmt: Image format ('PNG', 'JPEG').

    Returns:
        Base64-encoded string (without data URI prefix).
    """
    buffer = io.BytesIO()
    image.save(buffer, format=fmt)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def bytes_to_pil(data: bytes) -> Image.Image:
    """
    Convert raw bytes to a PIL Image.

    Args:
        data: Raw image bytes.

    Returns:
        PIL Image object.
    """
    return Image.open(io.BytesIO(data))


def resize_image(
    image: Image.Image,
    max_width: int = 640,
    max_height: int = 480,
) -> Image.Image:
    """
    Resize an image while maintaining aspect ratio.

    Args:
        image: PIL Image.
        max_width: Maximum width in pixels.
        max_height: Maximum height in pixels.

    Returns:
        Resized PIL Image.
    """
    image.thumbnail((max_width, max_height), Image.LANCZOS)
    return image


def validate_image(image: Image.Image) -> Tuple[bool, str]:
    """
    Validate that an uploaded image is suitable for face detection.

    Args:
        image: PIL Image object.

    Returns:
        Tuple of (is_valid, error_message).
    """
    if image is None:
        return False, "No image provided."

    min_dim = 50
    if image.width < min_dim or image.height < min_dim:
        return False, f"Image is too small ({image.width}×{image.height}). Minimum is {min_dim}×{min_dim} px."

    if image.mode not in ("RGB", "RGBA", "L", "P"):
        return False, f"Unsupported image mode: {image.mode}."

    return True, ""


def get_image_size_label(image: Image.Image) -> str:
    """
    Return a human-readable label for image dimensions.

    Args:
        image: PIL Image.

    Returns:
        String like '640 × 480 px'.
    """
    return f"{image.width} × {image.height} px"


def ensure_rgb(image: Image.Image) -> Image.Image:
    """Convert any PIL image mode to RGB."""
    return image.convert("RGB")


def clamp(value: float, min_val: float = 0.0, max_val: float = 100.0) -> float:
    """Clamp a float value between min and max."""
    return max(min_val, min(max_val, value))


def get_asset_path(filename: str) -> str:
    """
    Return the absolute path to a file in the assets directory.

    Args:
        filename: Asset file name.

    Returns:
        Absolute file path string.
    """
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "assets", filename)


def file_exists(path: str) -> bool:
    """Check whether a file exists at the given path."""
    return os.path.isfile(path)
