import wx.lib.plot
import wx.lib.plot.polyobjects
from wx.lib.plot import PolyLine, PlotCanvas, PlotGraphics

# https://wxpython.org/Phoenix/docs/html/wx.lib.plot.plotcanvas.PlotCanvas.html
# https://wxpython.org/Phoenix/docs/html/wx.lib.plot.polyobjects.html#module-wx.lib.plot.polyobjects 

# EXAMPLES:
# http://www.blog.pythonlibrary.org/2010/09/27/wxpython-pyplot-graphs-with-python/

def drawBarGraph():
    # Bar graph
    points1=[(1,0), (1,10)]
    line1 = PolyLine(points1, colour='green', legend='Feb.', width=10)
    points1g=[(2,0), (2,4)]
    line1g = PolyLine(points1g, colour='red', legend='Mar.', width=10)
    points1b=[(3,0), (3,6)]
    line1b = PolyLine(points1b, colour='blue', legend='Apr.', width=10)
 
    points2=[(4,0), (4,12)]
    line2 = PolyLine(points2, colour='Yellow', legend='May', width=10)
    points2g=[(5,0), (5,8)]
    line2g = PolyLine(points2g, colour='orange', legend='June', width=10)
    points2b=[(6,0), (6,4)]
    line2b = PolyLine(points2b, colour='brown', legend='July', width=10)
 
    return PlotGraphics([line1, line1g, line1b, line2, line2g, line2b],
                        "Bar Graph - (Turn on Grid, Legend)", "Months", 
                        "Number of Students")

class Plot(wx.Window):
    def __init__(self, _panel):
        super(wx.Window, self).__init__()

        panel = wx.Panel(parent=_panel, id=wx.ID_ANY)
        self.canvas = wx.lib.plot.PlotCanvas(panel)
        self.canvas.enableGrid = True

        # EXAMPLE
        #panel = wx.Panel(self, wx.ID_ANY)
        
        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        checkSizer = wx.BoxSizer(wx.HORIZONTAL)
 
        # create the widgets
        self.canvas.Draw(drawBarGraph())
        
        toggleGrid = wx.CheckBox(panel, label="Show Grid")
       # toggleGrid.Bind(wx.EVT_CHECKBOX, self.onToggleGrid)
        toggleLegend = wx.CheckBox(panel, label="Show Legend")
        #toggleLegend.Bind(wx.EVT_CHECKBOX, self.onToggleLegend)
 
        # layout the widgets
        mainSizer.Add(self.canvas, 1, wx.EXPAND)
        checkSizer.Add(toggleGrid, 0, wx.ALL, 5)
        checkSizer.Add(toggleLegend, 0, wx.ALL, 5)
        mainSizer.Add(checkSizer)
        panel.SetSizer(mainSizer)
        #EXAMPLE END

        

        self.Show()