from .polling import polling
from json import dumps
from functools import wraps

class telegram_types:
    def __init__(self):
        self.resetValues()
    
    def resetValues(self):
        self.chat_id = ''
        self.text = ''
    
    async def RunBOT(self):
        while True:
            try:
                out_polling = await polling()
                # Group
                if 'message' in out_polling:
                    with open('msg.json', 'w') as f:
                        f.write(dumps(out_polling, indent=2))
                        
                    self.chat_id = out_polling['message']['chat'].get('id','')
                    self.text = out_polling['message'].get('text','')
                return self    
            except:
                pass

Types = telegram_types()