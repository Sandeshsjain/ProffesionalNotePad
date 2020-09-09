import os
import speech_recognition as s
class Model:
    def __init__(self):
        self.key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset = 5
    def encrypt(self,plaintext):
        result = ""
        for a in plaintext:
            try:
                i = (self.key.index(a) + self.offset) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += a
        return result

    def decrypt(self,ciphertext):
        result = ""
        for a in ciphertext:
            try:
                i = (self.key.index(a)-self.offset) % len(self.key)
                result+=self.key[i]
            except ValueError:
                result+=a
        return result



    def save_file(self,msg,url):
        if type(url) is not str:
            file = url.name
        else:
            file = url


        filename,file_extension = os.path.splitext(file)
        if file_extension in '.ntxt':
            encrypted = self.encrypt(msg)
            with open(file,'w') as fw:
                fw.write(encrypted)

        else:
            with open(file,'w') as fw:
                fw.write(msg)


    def save_as(self,msg,url):
        if type(url) is not str:
            file = url.name

        else:
            file = url
        msg = self.encrypt(msg)
        with open(file,'w') as fw:
            fw.write(msg)



    def read_file(self,url):
        basename = os.path.basename(url)
        filename,file_extension = os.path.splitext(url)
        fi = open(url,"r")
        if file_extension in '.ntxt':
            with open(url,'r') as fi:
                msg1 = fi.read()
                decrypted = self.decrypt(msg1)
        else:
            with open(url,"r") as fi:
                decrypted = fi.read()
        return basename,decrypted


    def take_query(self):
        sr = s.Recognizer()
        sr.pause_threshold=1
        with s.Microphone() as m:
            audio = sr.listen(m)
            query = sr.recognize_google(audio,language='eng-in')
            return query

