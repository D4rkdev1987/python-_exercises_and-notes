class Invoice:
    
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100) # EVERYTHING IN PYTHON IS AN OBJECT REMEMBER-

print(google.client)      # to get access to the client value-prints Google

google.client = 'Yahoo'   # setting value Yahoo of the client-overriding using the SETTER process to set the value

print(google.client)      # from above it will print Goggle first and then since you overrode the client it will print yahoo