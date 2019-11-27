#   https://wxpython.org/pages/overview/

import wx
import UI.plot

class Frame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Frame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        ''' st = wx.StaticText(pnl, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # Add a Plot
        plot = UI.plot.Plot(pnl)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        sizer.Add(plot)
        #sizer.Add(plot, wx.SizerFlags().Border(wx.BOTTOM|wx.RIGHT, 25))
        pnl.SetSizer(sizer)'''

        # EXAMPLE
        panel = wx.Panel(pnl)
        self.canvas = wx.lib.plot.PlotCanvas(panel)
        self.canvas.enableGrid = True

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        checkSizer = wx.BoxSizer(wx.HORIZONTAL)

        # create the widgets
        self.canvas.Draw(UI.plot.drawBarGraph())
        toggleGrid = wx.CheckBox(panel, label="Show Grid")
        toggleLegend = wx.CheckBox(panel, label="Show Legend")

        # layout the widgets
        mainSizer.Add(self.canvas, 1, wx.EXPAND)
        checkSizer.Add(toggleGrid, 0, wx.ALL, 5)
        checkSizer.Add(toggleLegend, 0, wx.ALL, 5)
        mainSizer.Add(checkSizer)
        panel.SetSizer(mainSizer)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(panel, 1, wx.EXPAND)
        pnl.SetSizer(sizer)

    def makeMenuBar(self):
        return 0

    def OnExit(self, event):
        self.Close(True)