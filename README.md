# Inventree Part Deletion Tool
The Inventree Part Deletion Tool is a Python program that allows you to delete a list of parts from the Inventree database using the Inventree API. It is a simple and easy-to-use tool that helps you remove parts and their associated stock items from your inventory.

## Installation
To use the Inventree Part Deletion Tool, you need to have Python 3 installed on your system. You also need to install the inventree package which can be installed via pip. You can install this package by running the following command in your terminal or command prompt:
```shell
pip install -r requirements.txt
```

## Usage
To use the Inventree Part Deletion Tool, you need to provide a list of IPNs (Internal Part Numbers) in a text file named "input.txt" located in the same directory as the program.

Once you have the input file ready, you can run the program by navigating to the directory where the program is stored and running the following command:
```shell
$ python3 delete_parts.py
```
This will loop through each IPN in the input file and delete the corresponding part and all its associated stock items from the Inventree database.

Here's an example output for the given sample:
```shell
Item ID: 1234
Found 5 stock items
Tutto lo stock associato al Part con ID 1234 è stato eliminato.
The item with IPN TEST-1 has been deleted
Item ID: 5678
Found 0 stock items
The item with IPN TEST-2 has been deleted
```
This output shows that two parts have been deleted from the Inventree database. The first part had 5 associated stock items, which were also deleted. The second part had no associated stock items.

Please note that deleting parts and stock items from the Inventree database is a permanent action and cannot be undone. Please use this tool with caution and make sure that you have a backup of your data before proceeding.