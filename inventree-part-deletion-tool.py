import os
from dotenv import load_dotenv
from inventree.api import InvenTreeAPI
from inventree.part import Part
from inventree.stock import StockItem

# Load environment variables from .env file
load_dotenv()

# Specify the path to the file containing URLs
path = "input.txt"

# Create the file if it doesn't exist
if not os.path.exists(path):
    with open(path, "w") as f:
        pass

# Create an instance of the Inventree API
SERVER_ADDRESS = os.environ.get('INVENTREE_SERVER_ADDRESS')
MY_USERNAME = os.environ.get('INVENTREE_USERNAME')
MY_PASSWORD = os.environ.get('INVENTREE_PASSWORD')
api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME,
                   password=MY_PASSWORD, timeout=3600)

# Load the list of IPNs from the input file
with open(path, 'r') as f:
    ipn_list = [line.strip() for line in f]

# Loop through each IPN in the list
for ipn in ipn_list:

    # Extract the first 11 characters of the IPN
    ipn_to_compare = ipn[:11]

    # Call the function to get the list of items with the specified IPN
    item = Part.list(api, IPN__startswith=ipn_to_compare)

    # Check if any items were found
    if len(item) <= 0:
        print(f"The item with IPN {ipn} was not found")
        continue

    # Get the ID of the item from the item list
    item_id = item[0]['pk']
    print(f'Item ID: {item_id}')

    # Retrieve all StockItems associated with the Part
    stock_items = StockItem.list(api, part=item_id)
    print(f'Found {len(stock_items)} stock items')
    if len(stock_items) > 0:
        # Delete all StockItems associated with the Part
        StockItem.bulkDelete(api, [item['pk'] for item in stock_items])
        print(
            f"All stock associated with the Part with ID {item_id} has been deleted.")

    # Retrieve part instance with the specified ID
    part = Part(api, item_id)

    # Set the item to inactive
    # Update specified part parameters
    part.save(data={
        "active": False,
    })

    # Reload data from remote server
    part.reload()

    # Delete the item
    part.delete()

    print(f"The item with IPN {ipn} has been deleted")

    # Retrieve part instance with the specified ID
    part = Part(api, item_id)

    # Set the item to inactive
    # Update specified part parameters
    part.save(data={
        "active": False,
    })

    # Reload data from remote server
    part.reload()

    # Delete the item
    part.delete()

    print(f"The item with IPN {ipn} has been deleted")
