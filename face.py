import wx
import wx.lib.newevent
from array import array
import numpy as np
import random
import time
import pygame
import requests

URL_login = 'http://192.168.10.10/login'
URL_dump = 'http://192.168.10.10/dump'

login_data = dict(email='admin@syntronic.se', password='password')

coords =  np.zeros((2,8,16))
for x in range(0,8):
    for y in range(0,8):
        coords[0,y,x] = 25+x*(15+30)
        coords[0,y,x+8] = 430+x*(15+30)
        coords[1,y,x] = 67.5+y*(15+30)
        coords[1,y,x+8] = 67.5+y*(15+30)
        
def expressions(expr):
    expr_1 = np.zeros((8,16))
    if expr == 'full':
        expr_1 = np.ones((8,16))
    
    elif expr == 'angry':
        expr_1 = np.array(
        [[ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,      0.,  0.,  0.,  0.,  1.,  1.,  0.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,      0.,  0.,  0.,  1.,  1.,  1.,  1.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,      1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  0.,  0.,  1.,  1.,  0.,      0.,  1.,  1.,  0.,  0.,  1.,  1.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    elif expr == 'left':
        expr_1 = np.array(
        [[ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,      1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,      1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    elif expr == 'right':
        expr_1 = np.array(
        [[ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,      1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,      1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    elif expr == 'blink_right':
        expr_1 = np.array(
        [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,      1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.],
         [ 1.,  1.,  0.,  0.,  0.,  0.,  1.,  1.,      1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    elif expr == 'blink_left':
        expr_1 = np.array(
        [[ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
         [ 1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,      1.,  0.,  0.,  0.,  0.,  0.,  0.,  1.],
         [ 1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,      1.,  1.,  0.,  0.,  0.,  0.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
    elif expr == 'small_heart':
        expr_1 = np.array(
        [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
         [ 0.,  1.,  0.,  0.,  0.,  1.,  0.,  0.,      0.,  1.,  0.,  0.,  0.,  1.,  0.,  0.],
         [ 1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.,      1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  0.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,      0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.]])
    elif expr == 'heart':
        expr_1 = np.array(
        [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
         [ 0.,  1.,  0.,  0.,  0.,  1.,  0.,  0.,      0.,  1.,  0.,  0.,  0.,  1.,  0.,  0.],
         [ 1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.,      1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  0.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,      0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.]])
    
    return expr_1*coords

class MyPanel(wx.Panel):
 
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKey)
        self.timer = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.SetBackgroundColour("black")  
        
        pygame.init()
        self.path = '/home/jonathan/code/BB8_face/Audio/'
        self.formatType = '.wav'
    
        self.color = 0
        self.exp = 0
        self.expList = ['full', 'angry', 'left', 'right', 'blink_right', 'blink_left', 'small_heart', 'heart']
        
        self.db_id = 0
        self.text = ''     
        
        self.timer.Start(4000 + random.random() * 6000)
        
    def OnTimer(self, event):
        """ OnTimer event which is run at a random interval, which runs OnPaint method. """
        
        s = requests.session()
        s.post(URL_login, login_data)
        data = s.get(URL_dump)

        toArray = data.text
        array = toArray.split(',')
        array_name = []
        lastID = 1
        for i in range(len(array)):
            if i%2:
                array_name.append(array[i])
            else:
                lastID = int(array[i])
                
        if lastID > 1 and self.db_id == 0:
            self.db_id = lastID
            
        if self.db_id <= len(array_name)-1:
            self.text = array_name[self.db_id]
            self.Bind(wx.EVT_PAINT, self.OnWrite)
            self.db_id += 1
            filename = self.path + '0' + self.formatType
            pygame.mixer.Sound(filename).play().set_volume(1.0)
        else:
            self.exp = self.expList[random.randint(0, len(self.expList)-1)]
            self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        if random.randint(1,3) == 1:
            file = str(random.randint(1, 57))
            filename = self.path + file + self.formatType
            pygame.mixer.Sound(filename).play().set_volume(1.0)
        
        self.Refresh()

    def OnKey(self, event):
        """ Check for ESC key press and exit if ESC is pressed """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()
    
    def OnPaint(self, evt):
        """set up the device context (DC) for painting"""
        expr = expressions(self.exp)
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(wx.Colour(self.color), wx.SOLID))
        for i in range(0,8):
            for j in range(0,16):
                if expr[0,i,j] != 0:
#                     Todo: Replace DrawRectanlge with DrawRectangleList(self, rectangles, pens=None, brushes=None)
                    dc.DrawRectangle(expr[0,i,j], expr[1,i,j], 30, 30)
    
    def OnWrite(self, evt):
        """ Set up the device context (DC) for writing. """
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        fontStyle = wx.Font(wx.FontInfo(32).Family(wx.FONTFAMILY_MODERN))
        fontStyleL = wx.Font(wx.FontInfo(48).Family(wx.FONTFAMILY_MODERN))
        fontColour = wx.WHITE
        font = gc.CreateFont(fontStyle, fontColour)
        gc.SetFont(font)
        text1 = 'Thank you'
        text2 = 'for applying!'
        tw1, th1 = gc.GetTextExtent(text1)
        tw2, th2 = gc.GetTextExtent(text2)
        font = gc.CreateFont(fontStyleL, fontColour)
        gc.SetFont(font)
        tw, th = gc.GetTextExtent(self.text)
        font = gc.CreateFont(fontStyle, fontColour)
        gc.SetFont(font)
        gc.DrawText(text1, 400-tw1/2, 240-th/2-th1)
        gc.DrawText(text2, 400-tw2/2, 240-th/2+3/2*th2)
        font = gc.CreateFont(fontStyleL, fontColour)
        gc.SetFont(font)
        gc.DrawText(self.text, 400-tw/2, 240-th/2)
    
class MyFrame(wx.Frame):
    """Used for setting mode to fullscreen"""
 
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Robot demo, fullscreen")
        panel = MyPanel(self)
        self.ShowFullScreen(True)
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()    
