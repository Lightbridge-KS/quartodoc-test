def to_uppercase(text):
    """Convert a string to uppercase."""
    return text.upper()

def to_lowercase(text):
    """Convert a string to lowercase."""
    return text.lower()

def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]
