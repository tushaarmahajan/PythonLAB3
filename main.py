# main.py
from smart_scan_registration_module import RegisterUserFromSmartScan, display_image

# Path to the dummy SmartScan Code image
image_path = 'qr.jpeg'  # Replace with your actual image path if needed

# Display the dummy image
display_image(image_path)

# Register user from SmartScan Code
RegisterUserFromSmartScan(image_path)
