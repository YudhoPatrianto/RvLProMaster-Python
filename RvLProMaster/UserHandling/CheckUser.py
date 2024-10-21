# Load Library
from pathlib import Path

# Find Accepted User
find_accepteduser = next(Path(__file__).resolve().parent.parent.rglob("AcceptedUser.txt"))

class CheckUser:
    @staticmethod
    def Approval(user_id):
        user_id = str(user_id).strip()
        with open(f'{find_accepteduser}', 'r') as r:
            qq = ", ".join({line.strip() for line in r})
        return user_id in qq
