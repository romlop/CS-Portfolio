# Step 1: Assign the filename to a variable for clarity (Assuming "allow_list.txt" is file name with the IPs provided)
import_file = "allow_list.txt"

# Step 2: Open the file and read its content into a string variable
with open(import_file, 'r') as file:
    ip_addresses = file.read()  # Read the entire contents into 'ip_addresses'

# Step 3: Convert the 'ip_addresses' string into a list using the .split() method
ip_address_list = ip_addresses.split()

# Step 4: Assume the 'remove_list' is a list of IP addresses that should be removed from 'ip_address_list'
remove_list = ["192.168.10.2", "192.168.20.1", "10.10.0.2"]

# Step 5: Iterate through 'remove_list' to remove any matching IPs from 'ip_address_list'
for element in remove_list:
    if element in ip_address_list:
        ip_address_list.remove(element)

# Step 6: Convert the updated 'ip_address_list' back into a string, with each IP on a new line
updated_ip_addresses = "\n".join(ip_address_list)

# Write the updated IP list back to the file
with open(import_file, 'w') as file:
    file.write(updated_ip_addresses)

# Final output of updated ip_address_list for reference (for debugging or verification purposes)
print(updated_ip_addresses)
