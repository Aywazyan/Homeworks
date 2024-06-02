# URL Validator
# Write a function that validates a URL string. 
# Handle the ValueError by raising a custom exception if the URL format is invalid.

def validate_url(url):
    if not isinstance(url, str) or not url.startswith(("http://", "https://", "ftp://")):
        raise ValueError("Invalid URL format")

try:
    validate_url("http://www.example.com")
    print("Valid URL")
except ValueError as e:
    print(e)
