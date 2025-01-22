import re
from io import BytesIO

import pytesseract
import requests
from PIL import Image


def get_contract_address(text: str = "") -> str | None:
    evm_pattern = r"0x[a-fA-F0-9]{40}"
    solana_pattern = r"[1-9A-HJ-NP-Za-km-z]{32,44}"

    evm_match = re.search(evm_pattern, text, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    solana_match = re.search(
        solana_pattern, text, re.MULTILINE | re.IGNORECASE | re.DOTALL
    )

    if evm_match:
        return evm_match.group(0)
    elif solana_match:
        return solana_match.group(0)
    else:
        return None


def extract_text_from_image(image_url: str) -> str:
    with requests.request("GET", image_url) as response:
        img = Image.open(BytesIO(response.content))

    text = pytesseract.image_to_string(img)

    return text
