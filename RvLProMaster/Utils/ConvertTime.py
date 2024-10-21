# Load Library
import time

class ConvertTimeTo:
    class UnixTime():
        @staticmethod
        def oneday():
            Result1Days = int(time.time()) + 86400
            return Result1Days
        @staticmethod
        def oneweek():
            Result7Days = int(time.time()) + 604800
            return Result7Days
        @staticmethod
        def onemonth():
            Result30Days = int(time.time()) + 2592000
            return Result30Days