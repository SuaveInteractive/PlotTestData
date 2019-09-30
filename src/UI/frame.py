#   https://wxpython.org/pages/overview/

import wx

class Frame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Frame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

    def makeMenuBar(self):
        return 0


    def OnExit(self, event):
        self.Close(True)