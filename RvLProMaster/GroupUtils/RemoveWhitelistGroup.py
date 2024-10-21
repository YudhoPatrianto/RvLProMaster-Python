# Load Library
from pathlib import Path

# Find Accepted User
whitelist_group = next(Path(__file__).resolve().parent.parent.rglob("whitelist_group.txt"))

class DeleteWhitelistGroup:
    def Group(target_group):
        # Read Whitelist
        with open(whitelist_group, 'r') as read_whitelist:
            list_whitelist = read_whitelist.read()

        target_group = str(target_group)
        list_whitelist = list_whitelist.replace('', '')
        list_whitelist = list_whitelist.replace(target_group, '')
        
        # Delete
        with open(whitelist_group, 'w') as delete_whitelist:
            delete_whitelist.write(list_whitelist)