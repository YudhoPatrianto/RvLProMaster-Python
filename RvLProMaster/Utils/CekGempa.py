# Load Library
from httpx import AsyncClient, HTTPError, ReadTimeout

# CekGempa
class CekGempa:
    @staticmethod
    async def ObtainInfo(bmkg_get=None):
        url = 'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json'
        async with AsyncClient() as bmkg:
            fetch_bmkg = await bmkg.get(url)
            bmkg_get = fetch_bmkg.json()['Infogempa']['gempa']
            Tanggal = bmkg_get['Tanggal']
            Jam = bmkg_get['Jam']
            DateTime = bmkg_get['DateTime']
            Coordinates = bmkg_get['Coordinates']
            Lintang = bmkg_get['Lintang']
            Bujur = bmkg_get['Bujur']
            Magnitude = bmkg_get['Magnitude']
            Kedalaman = bmkg_get['Kedalaman']
            Wilayah = bmkg_get['Wilayah']
            Potensi = bmkg_get['Potensi']
            Dirasakan = bmkg_get['Dirasakan']
            Shakemap = f'https://data.bmkg.go.id/DataMKG/TEWS/{bmkg_get["Shakemap"]}'
            
            # Return Output
            return Tanggal, Jam, DateTime, Coordinates, Lintang, Bujur, Magnitude, Kedalaman, Wilayah, Potensi, Dirasakan, Shakemap