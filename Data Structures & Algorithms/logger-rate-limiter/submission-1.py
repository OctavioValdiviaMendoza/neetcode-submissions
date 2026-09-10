class Logger:

    def __init__(self):
        self.log_data = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        '''
        Dict = (key-> message, val ->timestamp)

        Check wheather message  is a duplicate:
            if duplicate check whether it is under 10s -> if under return False -> if over return true
        If not duplicate message should print
        '''
        if message in self.log_data:
            check_time = self.log_data.get(message)
            if timestamp >= check_time + 10:
                self.log_data[message] = timestamp
                return True
            else:
                return False
        else:
            self.log_data[message] = timestamp
            return True


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
