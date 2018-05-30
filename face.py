import wx
from array import array
import numpy as np

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
    elif expr == 'normal':
        expr_1 = np.array(
        [[ 0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,      1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,      1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.],
         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,      1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
         [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.],
         [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,      0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.]])
    return expr_1*coords

class MyPanel(wx.Panel):
 
    def __init__(self, parent, exp):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetBackgroundColour("black")
        self.exp = exp
 
    def onKey(self, event):
        """
        Check for ESC key press and exit if ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()
            
    def typeOfExpression():
        print(exp)
    
    def OnPaint(self, evt):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)
        expr = expressions('full')
        dc.SetBrush(wx.Brush(wx.Colour(255,255,255), wx.SOLID))
        for i in range(0,8):
            for j in range(0,16):
                if expr[0,i,j] != 0:
                    print(expr[0,i,j], expr[1,i,j], expr[0,i,j]+30, expr[1,i,j]+30)                    
                    dc.DrawRectangle(expr[0,i,j], expr[1,i,j], 30, 30)
        dc.EndDrawing()
        
class MyFrame(wx.Frame):
    """Used for setting mode to fullscreen"""
 
    def __init__(self, exp):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Robot demo, fullscreen")
        panel = MyPanel(self, exp)
        self.ShowFullScreen(True)
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame('full')
    app.MainLoop()
