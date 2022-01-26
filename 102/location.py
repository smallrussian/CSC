class Location:
    def __init__(self, row=0, col=0):
        self.row=row
        self.col=col
       
    @property
    def row(self):
        return self._row
    
    @row.setter
    def row(self, value):
        if value<0:
            value=0
        self._row=value
    
    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        if value<0:
            value=0
        self._col=value

    def __str__(self) -> str:
        return "({},{})".format(self.row, self.col)