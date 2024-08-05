# smartscan_registration_module.py
from PIL import Image

# In-Memory Storage: Simulate a database using a list of dictionaries
user_database = []

# Lambda functions for creating, inserting, and fetching user records
create_user_record = lambda name, email, destination, travel_date: {
    "name": name,
    "email": email,
    "destination": destination,
    "travel_date": travel_date
}
insert_user_record = lambda record: user_database.append(record)
fetch_all_users = lambda: user_database

# Function to simulate scanning and decoding SmartScan Code
def scan_smartscan_code(image_path):
    dummy_data = "Tushar Mahajan,tushar.mahajan@mca.christuniversity.in,Goa,2024-08-15"
    return dummy_data

# Function to register user from SmartScan
def RegisterUserFromSmartScan(image_path):
    user_data = scan_smartscan_code(image_path)
    if user_data:
        name, email, destination, travel_date = user_data.split(',')
        user_record = create_user_record(name, email, destination, travel_date)
        insert_user_record(user_record)
        print("User registered successfully!")
    else:
        print("Failed to scan the SmartScan Code.")
    
    print("All registered users:")
    for user in fetch_all_users():
        print(user)

# Function to display the dummy image
def display_image(image_path):
    img = Image.open(image_path)
    img.show()

if __name__ == "__main__":
    print("This is a module and should be imported to use the functions.")
