import wx
from array import array
import numpy

coords = np.matrix(
            [[ 0.  0.  1.  1.  1.  1.  0.  0.      0.  0.  1.  1.  1.  1.  0.  0.],
             [ 0.  1.  1.  1.  1.  1.  1.  0.      0.  1.  1.  1.  1.  1.  1.  0.],
             [ 1.  1.  1.  1.  1.  1.  1.  1.      1.  1.  1.  1.  1.  1.  1.  1.],
             [ 1.  1.  1.  0.  0.  1.  1.  1.      1.  1.  1.  0.  0.  1.  1.  1.],
             [ 1.  1.  1.  0.  0.  1.  1.  1.      1.  1.  1.  0.  0.  1.  1.  1.],
             [ 1.  1.  1.  1.  1.  1.  1.  1.      1.  1.  1.  1.  1.  1.  1.  1.],
             [ 0.  1.  1.  1.  1.  1.  1.  0.      0.  1.  1.  1.  1.  1.  1.  0.],
             [ 0.  0.  1.  1.  1.  1.  0.  0.      0.  0.  1.  1.  1.  1.  0.  0.]])

class MyPanel(wx.Panel):
 
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetBackgroundColour("black")
 
    def onKey(self, event):
        """
        Check for ESC key press and exit if ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()
    def expressions(expr):
        expr_1 = np.zeros((8,16))
        if expr="all":
            expr_1 = np.ones((8,16))
        elif expr="normal":
            expr_1 = np.matrix(
            [[ 0.  0.  1.  1.  1.  1.  0.  0.      0.  0.  1.  1.  1.  1.  0.  0.],
             [ 0.  1.  1.  1.  1.  1.  1.  0.      0.  1.  1.  1.  1.  1.  1.  0.],
             [ 1.  1.  1.  1.  1.  1.  1.  1.      1.  1.  1.  1.  1.  1.  1.  1.],
             [ 1.  1.  1.  0.  0.  1.  1.  1.      1.  1.  1.  0.  0.  1.  1.  1.],
             [ 1.  1.  1.  0.  0.  1.  1.  1.      1.  1.  1.  0.  0.  1.  1.  1.],
             [ 1.  1.  1.  1.  1.  1.  1.  1.      1.  1.  1.  1.  1.  1.  1.  1.],
             [ 0.  1.  1.  1.  1.  1.  1.  0.      0.  1.  1.  1.  1.  1.  1.  0.],
             [ 0.  0.  1.  1.  1.  1.  0.  0.      0.  0.  1.  1.  1.  1.  0.  0.]])
        return expr_1 = 
    
    def pixels(matrix,expr):
        expr = expressions(expr)
            
    def OnPaint(self, evt):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(wx.Colour(255,255,255), wx.SOLID))
        dc.DrawRectangle(10, 10, 50, 50)
        #self. 
        

class MyFrame(wx.Frame):
    """Used for setting full screen"""
 
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Robot demo, fullscreen")
        panel = MyPanel(self)
        self.ShowFullScreen(True)
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
