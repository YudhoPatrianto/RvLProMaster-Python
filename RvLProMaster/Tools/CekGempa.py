# Load Library
from httpx import AsyncClient
from json import dumps

endpoint_bmkg = 'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json'

@staticmethod
async def CekGempa():
    async with AsyncClient() as client:
        g = await client.get(endpoint_bmkg)
        data_bmkg = g.json()['Infogempa'].get('gempa', '')
        tanggal_gempa = data_bmkg.get('Tanggal', '')
        jam_gempa = data_bmkg.get('Jam', '')
        datetime_gempa = data_bmkg.get('DateTime', '')
        coordinate_gempa = data_bmkg.get('Coordinates', '')
        lintang_gempa = data_bmkg.get('Lintang', '')
        bujur_gempa = data_bmkg.get('Bujur', '')
        magnitude_gempa = data_bmkg.get('Magnitude', '')
        kedalaman_gempa = data_bmkg.get('Kedalaman', '')
        wilayah_gempa = data_bmkg.get('Wilayah', '')
        dirasakan_gempa = data_bmkg.get('Tanggal', '')
        shakemap_photo = f"https://data.bmkg.go.id/DataMKG/TEWS/{data_bmkg.get('Shakemap', '')}"
        return tanggal_gempa, jam_gempa, datetime_gempa, coordinate_gempa, lintang_gempa, bujur_gempa, magnitude_gempa, kedalaman_gempa, wilayah_gempa, dirasakan_gempa, shakemap_photo