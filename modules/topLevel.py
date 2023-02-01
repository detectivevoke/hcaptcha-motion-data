import random
import time

class topLevel():
    def __init__(self):
        self.t = {
                "inv": False,
                "st": 0,
                "sc": {
                    'availWidth': 1920,
                    'availHeight': 1040,
                    'width': 1920,
                    'height': 1080,
                    'colorDepth': 24,
                    'pixelDepth': 24,
                    'availLeft': 0,
                    'availTop': 0,
                    'onchange': None,
                    'isExtended': True
                },
                "nv": {
                    'vendorSub': '',
                    'productSub': '20030107',
                    'vendor': 'Google Inc.', 
                    'maxTouchPoints': 0, 
                    'scheduling': {}, 
                    'userActivation': {}, 
                    'doNotTrack': None, 
                    'geolocation': {}, 
                    'connection': {}, 
                    'pdfViewerEnabled': True, 
                    'webkitTemporaryStorage': {}, 
                    'hardwareConcurrency': 8, 
                    'cookieEnabled': True, 
                    'appCodeName': 'Mozilla', 
                    'appName': 'Netscape', 
                    'appVersion': '', 
                    'platform': 'Win32', 
                    'product': 'Gecko', 
                    'userAgent': '', 
                    'language': 'en-GB', 
                    'languages': ['en-GB', 'en-US', 'en'], 
                    'onLine': True, 
                    'webdriver': False, 
                    'bluetooth': {}, 
                    'clipboard': {}, 
                    'credentials': {}, 
                    'keyboard': {}, 
                    'managed': {}, 
                    'mediaDevices': {}, 
                    'storage': {}, 
                    'serviceWorker': {}, 
                    'virtualKeyboard': {}, 
                    'wakeLock': {}, 
                    'deviceMemory': 8, 
                    'ink': {}, 
                    'hid': {}, 
                    'locks': {}, 
                    'mediaCapabilities': {}, 
                    'mediaSession': {}, 
                    'permissions': {}, 
                    'presentation': {}, 
                    'serial': {}, 
                    'usb': {}, 
                    'windowControlsOverlay': {}, 
                    'xr': {},
                    "userAgentData": {
                        "brands": [
                            {"brand": "Not_A Brand", "version": "99"},
                            {"brand": "Google Chrome", "version": "109"},
                            {"brand": "Chromium", "version": "109"}
                        ],
                        "mobile": False,
                        "platform": "Windows"},
    
                    "plugins": ['internal-pdf-viewer', 'internal-pdf-viewer', 'internal-pdf-viewer', 'internal-pdf-viewer', 'internal-pdf-viewer']},
                    "dr": "https://www.google.com/",
                    "exec": False,
                    "wn": [],
                    "wn-mp": 0,
                    "mm": [],
                    "mm-mp": 0,
                    "v": 1}

    def agentMod(self, ua:str=None):
        self.t["nv"]["appCodeName"] = str(ua).split("/")[0]
        self.t["nv"]["appVersion"] = str(ua)[8:12]
        self.t["nv"]["userAgent"] = str(ua)

        return True
            
    def dataMod(self, data:dict={}):
        self.t["wn"] = [[1920, 1080, 1, int(time.time()) - 5]]
        #self.t["nv"]["xy"] = [[0, 0, 1, int(time.time()) - 5]]
        self.t["st"] = int(time.time())
        try:
            self.t["mm"] = data["mm"]
        except:
            return False
        return True

    def get(self):
            return self.t