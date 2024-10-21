# Load Library
from httpx import AsyncClient
import os


class Download:
    async def Image(target_url):
        """Download Image File From URL

        Args:
            target_url (str): Target Of URL You Wants Download
        """
        try:
            target_filetype = os.path.splitext(target_url)[-1]
            async with AsyncClient() as clientDownloader:
                r_clientDownloader = await clientDownloader.get(target_url)
                name_file = f'image{target_filetype}'
                with open(name_file, 'wb') as download_images:
                    download_images.write(r_clientDownloader.content)
        except:
            pass