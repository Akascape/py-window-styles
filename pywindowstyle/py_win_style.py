from ctypes import POINTER, pointer, sizeof, windll, Structure, byref, c_int
from ctypes.wintypes import DWORD, ULONG
import warnings
import sys

class ACCENT_POLICY(Structure):
        _fields_ = [
            ('AccentState',   DWORD),
            ('AccentFlags',   DWORD),
            ('GradientColor', DWORD),
            ('AnimationId',   DWORD),
        ]

class WINDOW_COMPOSITION_ATTRIBUTES(Structure):
        _fields_ = [
            ('Attribute',  DWORD),
            ('Data',       POINTER(ACCENT_POLICY)),
            ('SizeOfData', ULONG),
        ]

class apply_style():
    def __init__(self,
                 window,
                 style: str):

        if not sys.platform.startswith("win"):
            warnings.warn("Cannot apply header style! \nThis is not a windows environment.")
            return
        
        styles = ["dark", "mica", "aero", "transparent", "acrylic",
                  "win7", "inverse", "popup", "native", "optimised", "light"]
        if style not in styles:
            warnings.warn(f"Invalid Style! No such style exists: {style}")
            return
        
        window.update()
        self.HWND = windll.user32.GetParent(window.winfo_id())
        if style=="mica":
            ChangeHeader(self.HWND, 19, c_int(1))
            ChangeHeader(self.HWND, 1029, c_int(0x01))
        elif style=="optimised":
            ChangeAccent(self.HWND, 30, 1)
        elif style=="dark":
            ChangeHeader(self.HWND, 19, c_int(1))
        elif style=="light":
            ChangeHeader(self.HWND, 19, c_int(0))
        elif style=="inverse":
            ChangeAccent(self.HWND, 6, 1)
        elif style=="win7":
            ChangeAccent(self.HWND, 11, 1)
        elif style=="aero":
            window.config(bg="black")
            ChangeAccent(self.HWND, 30, 2)
            ChangeAccent(self.HWND, 19, 3, color=0x000000)
        elif style=="acrylic":
            window.config(bg="black")
            ChangeAccent(self.HWND, 30, 2)
            ChangeAccent(self.HWND, 19, 4, color=0x292929)
        elif style=="popup":
            ChangeAccent(self.HWND, 4, 1)
        elif style=="native":
            ChangeAccent(self.HWND, 30, 2)
            ChangeAccent(self.HWND, 19, 2)
        elif style=="transparent":
            window.config(bg="black")
            ChangeAccent(self.HWND, 30, 2)
            ChangeAccent(self.HWND, 19, 4, color=0)
      
class change_header_color():
    def __init__(self,
                 window,
                 string: str=None,
                 red: int=10,
                 green: int=10,
                 blue: int=10):
        
        if not sys.platform.startswith("win"):
            warnings.warn("Cannot apply header style! This is not a windows environment.")
            return
        
        window.update()
       
        if blue>=100:
            blue="FF"
        if green>=100:
            green="FF"
        if red>=100:
            red="FF"

        self.HWND = windll.user32.GetParent(window.winfo_id())
        if string=="transparent":
            ChangeAccent(self.HWND, 30, 2)
            return
        else:
            ChangeAccent(self.HWND, 30, 0)
            
        self.color = f"{blue}{green}{red}" if not string else string
        self.color = DWORD(int(self.color, base=16))
        self.attrib = 35
        ChangeHeader(self.HWND, self.attrib, self.color)
        
            
class change_border_color():
    def __init__(self,
                 window,
                 string: str=None,
                 red: int=10,
                 green: int=10,
                 blue: int=10):
        
        if not sys.platform.startswith("win"):
            warnings.warn("Cannot apply header style! This is not a windows environment.")
            return
        
        window.update()
        
        if blue>=100:
            blue="FF"
        if green>=100:
            green="FF"
        if red>=100:
            red="FF"
            
        self.HWND = windll.user32.GetParent(window.winfo_id())
        self.color = f"{blue}{green}{red}" if not string else string
        self.color = DWORD(int(self.color, base=16))
        self.attrib = 34
        ChangeHeader(self.HWND, self.attrib, self.color)
        
class change_title_color():
    def __init__(self,
                 window,
                 string: str=None,
                 red: int=10,
                 green: int=10,
                 blue: int=10):
        
        if not sys.platform.startswith("win"):
            warnings.warn("Cannot apply header style! This is not a windows environment.")
            return
        
        window.update()
        
        if blue>=100:
            blue="FF"
        if green>=100:
            green="FF"
        if red>=100:
            red="FF"
            
        self.HWND = windll.user32.GetParent(window.winfo_id())
        self.color = f"{blue}{green}{red}" if not string else string
        self.color = DWORD(int(self.color, base=16))
        self.attrib = 36
        ChangeHeader(self.HWND, self.attrib, self.color)
        
def ChangeHeader(hWnd, attrib, color):
    windll.dwmapi.DwmSetWindowAttribute(hWnd, attrib, byref(color), sizeof(c_int))
        
def ChangeAccent(hWnd: int, attrib, state, color=None):                                           
    accentPolicy = ACCENT_POLICY()  
                                                
    winCompAttrData = WINDOW_COMPOSITION_ATTRIBUTES()
    winCompAttrData.Attribute = attrib
    winCompAttrData.SizeOfData = sizeof(accentPolicy)
    winCompAttrData.Data = pointer(accentPolicy)

    accentPolicy.AccentState =  state
    if color:
        accentPolicy.GradientColor = color
                                    
    windll.user32.SetWindowCompositionAttribute(hWnd, pointer(winCompAttrData))
