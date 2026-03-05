import pytesseract

def extract_text(image):
    """
    Extract raw text from the preprocessed image using pytesseract.
    """
    text = pytesseract.image_to_string(image)
    return text