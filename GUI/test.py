from PyQt5 import QtWidgets, QtCore, QtGui

class DrawImage(QtWidgets.QWidget):    
    def __init__(self):
        super(DrawImage, self).__init__()

        self.move(150,50)
        self.setFixedSize(100,100)   
        self.startA    = 5
        self.endA      = 30
        self.linewidth = 1

    def paintEvent(self, event):                                 #use to draw on the canvas
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(QtCore.Qt.white)
        paint.drawRect(event.rect())        


        # +++
        paint.setPen(QtCore.Qt.red)                      
        paint.setBrush(QtCore.Qt.white)   
        paint.drawArc(15, 15, 70, 70, 0 * 16, -180 * 16)         # <-----------        


        paint.setPen(QtCore.Qt.black)
        paint.setBrush(QtCore.Qt.white)   
        paint.drawEllipse(QtCore.QRect(25, 25, 50, 50))           #outer circle

        paint.setPen(QtCore.Qt.yellow)
        paint.setBrush(QtCore.Qt.yellow)   
        paint.drawEllipse(QtCore.QRect(37.5, 37.5, 25, 25))       #  middle circle

        paint.setPen(QtCore.Qt.blue)  # white
        paint.setBrush(QtCore.Qt.white)   
        paint.drawEllipse(QtCore.QRect(43.75, 43.75, 12.5, 12.5)) #innermost circle

        #where I am trying to implement a half circle
        r = QtCore.QRect(12.5, 12.5, 20, 20)                       #<-- create rectangle
        size = r.size()                                            #<-- get rectangle size
        r.setSize(size*10)                                         #<-- set size
        startAngle = self.startA*16                                #<-- set start angle to draw arc
        endAngle = self.endA*16                                    #<-- set end arc angle
        paint.setPen(QtGui.QPen(QtGui.QColor('#000000'), self.linewidth))   #<-- arc color
        paint.setBrush(QtCore.Qt.yellow)   
        paint.drawArc(r, startAngle, endAngle)      

        paint.end()    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = DrawImage()
    w.show()
    sys.exit(app.exec_())