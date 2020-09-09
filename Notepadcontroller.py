import Notepadmodel
class Controller:
    def __init__(self):
        self.model = Notepadmodel.Model()

    def save_file(self,msg,url):
        self.model.save_file(msg,url)

    def save_as(self,msg,url):
        self.model.save_as(msg,url)

    def read_file(self,url):
        self.result , self.decrypted = self.model.read_file(url)
        return self.result,self.decrypted

    def take_query(self):
        self.takeAudio = self.model.take_query()
        return self.takeAudio