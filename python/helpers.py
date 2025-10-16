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


def read_local_pdf_base64(file_path: str) -> str:
    """Read a local PDF file and return it as base64."""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
