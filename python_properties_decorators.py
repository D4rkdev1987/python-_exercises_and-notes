class Invoice:
    
    def __init__(self, client, total):
        self._client = client                  # both client and total protected by the underscore
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'
    # anytime you deal with data you use underscores to protect the data(data attribute should be protected _client)-the child classes have access to data
    @property                   # property decorator-user the at symbol-it decorates the property we want to work with
    def client(self):           # create the function called client-then pass in self
        return self._client     # now return self._client (given a clear distintion on how to treat the invoice-most likely want to access at one point to directly call)

    @client.setter              # setter values-you don't want to ovveride the total-say at then the value you want to ovveride
    def client(self, client):   # create the function now client pass in self and client
        self._client = client   # now to override the value in the class

    @property                   # now property decortaor for the total below same as client
    def total(self):            
        return self._total       

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'  # overriding the client to yahoo because we have allowed it in the setter 

print(google.client)