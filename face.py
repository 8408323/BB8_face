import wx
import wx.lib.newevent
from array import array
import numpy as np
import random
import time
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


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
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,      1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,      1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    elif expr == 'right':
        expr_1 = np.array(
        [[ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,      1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,      1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    elif expr == 'blink_right':
        expr_1 = np.array(
        [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
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
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        self.timer = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.SetBackgroundColour("black")  
    
        self.color = 0
        self.exp = 0
        self.expList = ['full', 'angry', 'left', 'right', 'blink_right', 'blink_left', 'small_heart', 'heart']
        
        self.db_id = 0
        self.text = ''     
        
        self.timer.Start(4000 + random.random() * 6000)
        
    def OnTimer(self, event):
        """ OnTimer event which is run at a random interval, which runs OnPaint method. """
        
        self.db = MySQLdb.connect(host="192.168.10.10",
                             user="homestead",
                             passwd="secret",
                             db="laravel_exjobb")
        self.cur = self.db.cursor()
        self.cur.execute("SELECT * FROM registration")
        
        name_ls = []
        for row in self.cur.fetchall():
            name_ls.append(row[1])
            
        if self.db_id <= len(name_ls)-1:
            self.text = name_ls[self.db_id]
            print(self.text)
#             self.Bind(self.EVT_WRITE, self.OnWrite)
            self.Bind(wx.EVT_PAINT, self.OnWrite)
            self.db_id = self.db_id + 1
        else:                
            self.exp = self.expList[random.randint(0, len(self.expList)-1)]
            self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Refresh()

    def onKey(self, event):
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
        fontColour = wx.WHITE
        font = gc.CreateFont(fontStyle, fontColour)
        gc.SetFont(font)
        tw, th = gc.GetTextExtent(self.text)
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
