# Load Library
import speedtest

# Start Speedtest
class Speedtest:
    @staticmethod
    def Active():
        speedtest_client = speedtest.Speedtest()
        servers = speedtest_client.get_best_server()
        # Get Information
        download = f'{speedtest_client.download() / 10**6:.2f}'
        upload = f'{speedtest_client.upload() / 10**6:.2f}'
        ping = f'{speedtest_client.results.ping:.0f}'
        isp = speedtest_client.results.client['isp']
        provider = servers['sponsor']
        location = servers['name']
        speedtest_picture = speedtest_client.results.share()
        
        # Show Result
        return download, upload, ping, provider, isp, location , speedtest_picture