import random
import time

class topLevel():
    def __init__(self):
        self._top = {
            "inv": "false",
            "st": "",
            "sc": {
                "availWidth": 1920,
                "avaiHeight": 1040,
                "width": 1920,
                "height": 1080,
                "colorDepth": 24,
                "pixelDepth": 24,
                "availLeft": 0,
                "availTop": 0,
                "onchange": "null",
                "isExtended": "true"
            },
            "nv": {
                "vendorSub": "",
                "productSub": "20030107",
                "vendor": "Google Inc.",
                "maxTouchPoints": 0,
                "scheduling": {},
                "userActivation": {},
                "doNotTrack": "null",
                "geolocation": {},
                "connection": {},
                "pdfViewerEnabled": "true",
                "webkitTemporaryStorage": {},
                "hardwareConcurrency": 8,
                "cookieEnabled": "true",
                "appCodeName": "",
                "appName": "Netscape",
                "appVersion": "",
                "platform": "Win32",
                "product": "Gecko",
                "userAgent": "",
                "language": "en-GB",
                "languages": [
                    "en-GB",
                    "en-US"
                ],
                "onLine": "True",
                "webdriver": "false",
                "bluetooth": {},
                "clipboard": {},
                "credentials": {},
                "keyboard": {},
                "managed": {},
                "mediaDevices": {},
                "storage": {},
                "serviceWorker": {},
                "virtualKeyboard": {},
                "wakeLock": {},
                "deviceMemory": 8,
                "ink": {},
                "hid": {},
                "locks": {},
                "mediaCapabilities": {},
                "mediaSession": {},
                "permissions": {},
                "presentation": {},
                "serial": {},
                "usb": {},
                "windowControlsOverlay": {},
                "xr": {},
                "userAgentData": {
                    "brands": [
                        {
                            "brand":"Not?A_Brand",
                            "version": "8",   
                        },
                        {
                            "brand": "Chromium",
                            "version": "108"
                        },
                        {
                            "brand": "Google Chrome",
                            "version": "108",
                        }
                    ],
                    "mobile": "false",
                    "platform": "",
                    "plugins": ["internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer"]
                },
                "dr": "https://www.google.com",
                "exec": "false",
                "wn": [],
                "wn-mp": 0,
                "xy": [],
                "xy-mp": 0,
                "mm": [],
                "mm-mp": 0,
                "md": [],
                "md-mp": 0,
                "mu": [],
                "mu-mp": 0,
            }
        }

    def agentMod(self, ua:str=None):
        self._top["nv"]["appCodeName"] = ua.split("/")[0]
        self._top["nv"]["appVersion"] = ua[8:12]
        self._top["nv"]["userAgent"] = ua

        return True

    def dataMod(self, data:dict={}):
        self._top["nv"]["wn"] = [[1920, 1080, 1, int(time.time()) - 5]]
        self._top["nv"]["xy"] = [[0, 0, 1, int(time.time()) - 5]]

        self._top["st"] = random.randint(100,400)

        try:
            self._top["nv"]["mm"] = data["mm"]
            
        except:
            return False

        return True

    def get(self):
        return self._top
