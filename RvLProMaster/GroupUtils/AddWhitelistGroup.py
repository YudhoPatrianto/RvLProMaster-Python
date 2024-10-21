# Load Library
from pathlib import Path

# Find Accepted User
whitelist_group = next(Path(__file__).resolve().parent.parent.rglob("whitelist_group.txt"))

class AddWhitelistGroup:
    def Group(target_group):
        with open(whitelist_group, 'a') as write_group:
            write_group.write(f'{target_group}\n')