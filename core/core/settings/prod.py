from .base import *

DEBUG = False

# Security headers
SECURE_BROWSER_XSS_FILTER = True  # Helps prevent some XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Stops the browser from MIME-sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking