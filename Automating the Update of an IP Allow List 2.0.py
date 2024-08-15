import os
import logging

# Set up logging
logging.basicConfig(filename='update_ip_list.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

def backup_file(file_path):
    backup_path = f"{file_path}.backup"
    try:
        os.rename(file_path, backup_path)
        logging.info(f"Backup created: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")

def update_ip_list(import_file, remove_list):
    try:
        # Step 1: Backup the original file
        backup_file(import_file)

        # Step 2: Open the file and read its content into a string variable
        with open(import_file, 'r') as file:
            ip_addresses = file.read()  # Read the entire contents into 'ip_addresses'

        # Step 3: Convert the 'ip_addresses' string into a list using the .split() method
        ip_address_list = ip_addresses.split()

        # Step 4: Iterate through 'remove_list' to remove any matching IPs from 'ip_address_list'
        for element in remove_list:
            if element in ip_address_list:
                ip_address_list.remove(element)
                logging.info(f"Removed IP: {element}")

        # Step 5: Convert the updated 'ip_address_list' back into a string, with each IP on a new line
        updated_ip_addresses = "\n".join(ip_address_list)

        # Step 6: Write the updated IP list back to the file
        with open(import_file, 'w') as file:
            file.write(updated_ip_addresses)
        
        logging.info("IP allow list successfully updated.")
        return True

    except Exception as e:
        logging.error(f"Error updating IP list: {e}")
        return False

# Example usage
remove_list = [
    "192.168.10.2", "192.168.20.1", "10.10.0.2"
]

if update_ip_list("allow_list.txt", remove_list):
    print("Update successful.")
else:
    print("Update failed.")
