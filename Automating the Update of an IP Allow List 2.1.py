import os
import logging

# Set up logging
logging.basicConfig(filename='update_ip_list.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# Example list of IPs to be removed
remove_list = [
    "192.168.10.2", "192.168.20.1", "10.10.0.2"
]

def backup_file(file_path):
    backup_path = f"{file_path}.backup"
    try:
        os.rename(file_path, backup_path)
        logging.info(f"Backup created: {backup_path}")
        return backup_path  # Return the path of the backup file
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        print(f"Failed to create backup: {e}")  # Debugging output
        return None

def update_ip_list(import_file, remove_list):
    try:
        # Step 1: Backup the original file and use the backup file for further operations
        backup_path = backup_file(import_file)
        if not backup_path:
            raise FileNotFoundError("Backup failed, cannot proceed.")

        # Step 2: Open the backup file and read its content into a string variable
        with open(backup_path, 'r') as file:
            ip_addresses = file.read()  # Read the entire contents into 'ip_addresses'

        # Step 3: Convert the 'ip_addresses' string into a list using the .split() method
        ip_address_list = ip_addresses.split()

        # Step 4: Iterate through 'remove_list' to remove any matching IPs from 'ip_address_list'
        for element in remove_list:
            if element in ip_address_list:
                ip_address_list.remove(element)
                logging.info(f"Removed IP: {element}")
                print(f"Removed IP: {element}")  # Debugging output

        # Step 5: Convert the updated 'ip_address_list' back into a string, with each IP on a new line
        updated_ip_addresses = "\n".join(ip_address_list)

        # Step 6: Write the updated IP list back to the original file (creating a new one)
        with open(import_file, 'w') as file:
            file.write(updated_ip_addresses)
        
        logging.info("IP allow list successfully updated.")
        print("Update successful.")  # Debugging output
        return True

    except Exception as e:
        logging.error(f"Error updating IP list: {e}")
        print(f"Error: {e}")  # Debugging output
        return False

# Run the update_ip_list function with the specified remove_list
if update_ip_list("allow_list.txt", remove_list):
    print("Update successful.")
else:
    print("Update failed.")
