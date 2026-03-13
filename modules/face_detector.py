"""
face_detector.py
Handles face detection from images using OpenCV Haar Cascades.
"""

import cv2
import numpy as np
from PIL import Image
from typing import Optional, Tuple, List


def load_face_cascade() -> cv2.CascadeClassifier:
    """Load OpenCV's pre-trained Haar Cascade for face detection."""
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    return face_cascade


def detect_faces(image: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """
    Detect all faces in the given image.

    Args:
        image: NumPy array (BGR or RGB format).

    Returns:
        List of bounding boxes (x, y, w, h) for each detected face.
    """
    face_cascade = load_face_cascade()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )
    if len(faces) == 0:
        return []
    return [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in faces]


def draw_face_box(image: np.ndarray, faces: List[Tuple[int, int, int, int]]) -> np.ndarray:
    """
    Draw bounding boxes around detected faces.

    Args:
        image: Original image as NumPy array (RGB).
        faces: List of (x, y, w, h) tuples.

    Returns:
        Image with drawn bounding boxes.
    """
    annotated = image.copy()
    for x, y, w, h in faces:
        cv2.rectangle(annotated, (x, y), (x + w, y + h), (108, 99, 255), 2)
        cv2.putText(
            annotated,
            "Face",
            (x, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (108, 99, 255),
            2,
        )
    return annotated


def pil_to_cv2(pil_image: Image.Image) -> np.ndarray:
    """Convert a PIL Image to a NumPy array in BGR format."""
    rgb = np.array(pil_image.convert("RGB"))
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)


def cv2_to_pil(cv2_image: np.ndarray) -> Image.Image:
    """Convert a NumPy array (BGR) to a PIL Image (RGB)."""
    rgb = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)


def get_largest_face(faces: List[Tuple[int, int, int, int]]) -> Optional[Tuple[int, int, int, int]]:
    """
    Return the largest detected face (by area).

    Args:
        faces: List of (x, y, w, h) tuples.

    Returns:
        The largest face tuple, or None if list is empty.
    """
    if not faces:
        return None
    return max(faces, key=lambda f: f[2] * f[3])


def crop_face(image: np.ndarray, face: Tuple[int, int, int, int], padding: int = 20) -> np.ndarray:
    """
    Crop the face region from the image with optional padding.

    Args:
        image: NumPy array.
        face: (x, y, w, h) tuple.
        padding: Extra pixels around the face bounding box.

    Returns:
        Cropped face image as NumPy array.
    """
    x, y, w, h = face
    h_img, w_img = image.shape[:2]
    x1 = max(0, x - padding)
    y1 = max(0, y - padding)
    x2 = min(w_img, x + w + padding)
    y2 = min(h_img, y + h + padding)
    return image[y1:y2, x1:x2]
