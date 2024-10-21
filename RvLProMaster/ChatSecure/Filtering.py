# Load Library
from pathlib import Path
import re

class FilterChat:
    # Badword
    class Badword:
        def __init__(self):
            query_list = next(Path(__file__).resolve().parent.parent.rglob("badword.txt"))
            self.query_file = Path(query_list)
            self.pattern = self.initializing_pattern()
            
        def initializing_pattern(self):
            with self.query_file.open('r') as f:
                pattern = f.readlines()
                
            c = '|'.join([p.strip() for p in pattern])
            return c
        
        def ChatUser(self, chat_users):
            return bool(re.findall(self.pattern, chat_users))
    # Anti Kriptod
    class Kriptod:
        def __init__(self):
            query_list = next(Path(__file__).resolve().parent.parent.rglob("btc.txt"))
            self.query_file = Path(query_list)
            self.pattern = self.initializing_pattern()
            
        def initializing_pattern(self):
            with self.query_file.open('r') as f:
                pattern = f.readlines()
                
            c = '|'.join([p.strip() for p in pattern])
            return c
        
        def ChatUser(self, chat_users):
            return bool(re.findall(self.pattern, chat_users))
        
FilterChat.Kriptod().ChatUser