# Load Library
import re
from pathlib import Path

# Search ListBadword
ListBadwordFile = next(Path(__file__).resolve().parent.parent.rglob("badword.txt"))

class AddBadword:
    def Target(Badword):
        try:
            regex_word = {
                "a": "['aA4']", "b": "['bB8']", "c": "['cC']", "d": "['dD']", "e": "['eE3']",
                "f": "['fF']", "g": "['gG']", "h": "['hH']", "i": "['iI1']", "j": "['jJ']", 
                "k": "['kK']", "l": "['lL']", "m": "['mM']", "n": "['nN']", "o": "['oO0']", 
                "p": "['pP']", "q": "['qQ']", "r": "['rR']", "s": "['sS5']", "t": "['tT']", 
                "u": "['uU']", "v": "['vV']", "w": "['wW']", "x": "['xX']", "y": "['yY']", "z": "['zZ']"
            }
            AutoRegex = ''.join(regex_word.get(rg.lower(), rg) for rg in Badword)
            with open(ListBadwordFile, 'a') as WriteBadword:
                WriteBadword.write(f'\n{AutoRegex}')
        except StopIteration as errsi:
            print(f"Unable To Add To Filter: {errsi}")