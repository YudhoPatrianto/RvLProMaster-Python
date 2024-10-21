# Load Library
from pathlib import Path

# Find Accepted User
whitelist_group = next(Path(__file__).resolve().parent.parent.rglob("whitelist_group.txt"))

class CheckGroup:
    @staticmethod
    def Whitelist(target_group):
        target_group = str(target_group).strip()
        with open(f'{whitelist_group}', 'r') as rs:
            qqr = ", ".join({lines.strip() for lines in rs})
        return target_group in qqr
