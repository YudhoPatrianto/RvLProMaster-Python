from .polling import polling
from json import dumps
from typing import Optional

class telegram_types:
    def __init__(self):
        self.resetValues()
    
    def resetValues(self):
        self.chat_id = ''
        self.text = ''
        self.chat_position = ''
        
    # Save Polling 
    def savePolling(self, out_polling):
        if 'message' in out_polling:
            with open('message.json', 'w') as f:
                f.write(dumps(out_polling, indent=2))
        elif 'channel_post' in out_polling:
            with open('channel.json', 'w') as f:
                f.write(dumps(out_polling, indent=2))

    async def RunBOT(self, save_polling: Optional[bool] = False):
        while True:
            try:
                out_polling = await polling()
                # Group
                if 'message' in out_polling:
                    self.chat_id = out_polling['message']['chat'].get('id','')
                    self.text = out_polling['message'].get('text','')
                    # Save Polling
                    if save_polling == True:
                        self.savePolling(out_polling)
                    else:
                        pass
                return self    
            except:
                pass

Types = telegram_types()