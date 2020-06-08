import os
import hashlib
import requests




LANG = {'en':'English', 'es':'Spanish', 'pt':'Portuguese', 'fr':'French'}
EXT = ['.mkv', '.mp4', '.wav', '.wmv', '.flv']
tempLang = []

class Subtitle:

    url = "http://api.thesubdb.com/"
    headers = {"User-Agent":"SubDB/1.0 (PySub/0.1; localhost)"}
    

    def verifier(self):
        if self.videoExtension not in EXT:
            return False
        else:
            return True


    def setVideo(self, video):
        self.videoName = os.path.splitext(video)[0]
        self.videoExtension = os.path.splitext(video)[1]
        self.hash = self.getHash(video)

    def getHash(self, name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

    def getLang(self, verbose=False):
        global tempLang
        if self.verifier():        
            url = self.url + f"?action=search&hash={self.hash}"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                if not verbose:
                    return response.text
                else:
                    tempLang = response.text.split(',')
                    print(tempLang)
                    _list_ = [LANG[i] for i in tempLang]
                    return f"Found: {', '.join(str(x) for x in _list_)}"
            else:
                return f"Not Found: {response.status_code}"
        else:
            print('Fail')
            return None

    def getSub(self, lang, newname=None):

        name = self.videoName if newname is None else os.path.dirname(self.videoName)+ "/" + newname
        print(name)
        global tempLang
        try:
            if self.verifier():
                revL = {y: x for x, y in LANG.items()}[lang]
                if revL in tempLang:
                    url = self.url + f"?action=download&hash={self.hash}&language={revL}"
                    response = requests.get(url, headers=self.headers)
                    with open(name+'.srt', 'w', encoding=response.encoding) as f:
                        f.write(response.text)
                        print("Downloaded with success")
                else:
                    print("RevL: ", revL, "\ntemplang: ", tempLang)
                    return None
            else:
                print('Fail')
                return None
        except Exception as e:
            with open("log.txt", "a") as f:
                f.write(str(e) + "\n")
    
        


if __name__ == "__main__":
    # Using tkinter here just for debugging purposes.
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    inst = Subtitle()
    Tk().withdraw()
    inst.setVideo(askopenfilename())
    inst.getLang(verbose=True)
    inst.getSub("English", newname="subtitle")

