import base64

import httpx


def fetch_image_base64(url: str) -> str:
    """Fetch an image from a URL and return it as base64."""
    response = httpx.get(url)
    return base64.b64encode(response.content).decode("utf-8")


def fetch_pdf_base64(url: str) -> str:
    """Fetch a PDF from a URL and return it as base64."""
    response = httpx.get(url)
    return base64.b64encode(response.content).decode("utf-8")
