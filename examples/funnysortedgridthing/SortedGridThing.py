import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.DisclosurePanel import DisclosurePanel

class OddGridWidget(DockPanel):

    def __init__(self, **kwargs):
        DockPanel.__init__(self, **kwargs)
        self.grid = Grid(StyleName="datagrid")
        self.sp = ScrollPanel(self.grid, Width="100%", Height="100%")
        self.header = Grid(Height="50px")
        self.add(self.header, DockPanel.NORTH)
        self.add(self.sp, DockPanel.CENTER)
        cf = self.setCellHeight(self.header, "50px")
        cf = self.setCellHeight(self.sp, "100%")

    def setData(self, data):
        rows = len(data)
        cols = 0
        if rows > 0:
            cols = len(data[0])
        self.grid.resize(rows, cols)
        for (nrow, row) in enumerate(data):
            for (ncol, item) in enumerate(row):
                self.grid.setHTML(nrow, ncol, str(item))

data = [["hello", "fred", 52],
        ["bye", "joe", 98],
        ["greetings", "alien", 0],
        ["sayonara", "jun", 1],
        ["gutentaag", "volker", 2],
        ["bonjour", "francois", 5],
        ["au reservoir", "fabrice", 8],
        ["go away", "mary", 73]
       ]

if __name__ == '__main__':
    pyjd.setup("public/SortedGridThing.html")
    ogw = OddGridWidget(Width="600px", Height="200px", StyleName="ogw")
    ogw.setData(data)
    RootPanel().add(ogw)
    pyjd.run()

