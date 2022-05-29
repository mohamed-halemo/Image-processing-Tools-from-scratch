from PyQt5 import QtWidgets,QtGui,QtCore
from ImageView2Tabs import Ui_MainWindow
import sys
from PyQt5.QtGui import *
from PIL import Image,ImageColor,ExifTags
import os
import matplotlib
from numpy import asarray
import cv2
import matplotlib.pyplot as plt
import pyqtgraph as pg
import pydicom
matplotlib.use('Qt5Agg')
import matplotlib.animation as animation
from pydicom.data import get_testdata_files
from PyQt5.QtWidgets import QFrame, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as Navi
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import struct
from matplotlib.figure import Figure
import numpy as np
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Browser=self.ui.Browse
        self.OutputImage=self.ui.Image
        self.Info=self.ui.Info
        # self.Info.setFrameShape(QFrame.Panel)
        self.ShowBtn=self.ui.ShowPixels
        self.Tab2OutPut=self.ui.Tab2Label
        self.GenerateBTN=self.ui.GenerateBtn
        self.ShowBtn.clicked.connect(self.ShowPixels)
        self.Browser.clicked.connect(self.Browse)
        self.GenerateBTN.clicked.connect(self.Generate)
        self.fig2,self.ax2 = plt.subplots(1,1)
        self.lay2=QtWidgets.QVBoxLayout(self.Tab2OutPut)
        
        self.fig,self.ax1 = plt.subplots(1,1)
        self.fig.subplots_adjust(left=0,bottom=0,right=1,top=1,wspace=None,hspace=None)
        
        self.lay=QtWidgets.QVBoxLayout(self.OutputImage)

        self.plotWidget2=FigureCanvas(self.fig2)
        # self.lay2.addWidget(self.plotWidget2)

        self.msg = QMessageBox()
        self.msg.setWindowTitle("Error")
        self.Bool=0
        self.Bool2=1
    def Browse(self):
        FileName=QtWidgets.QFileDialog.getOpenFileName(self,"Open File","E:\\Year3 Term1\\Image Processing\\Task1","All Files (*);;PNG Files (*.png);;Jpg Files(*.jpg);; Bmp Files(*.bmp)")
        
        filename, file_extension = os.path.splitext(FileName[0])
        print(file_extension+"HIIIII")
        
        if(file_extension=='.dcm' or file_extension=='.DCM'):
            try:
                
                if self.Bool==0:
                    self.plotWidget=FigureCanvas(self.fig)
                self.Bool=1
                self.OutputImage.clear()
                ds = pydicom.dcmread(FileName[0])
                dsInfo=pydicom.read_file(FileName[0])
                
                # print(dir(dsInfo))
                # print(str(ds))
                self.lay.addWidget(self.plotWidget)
                im = Image.fromarray(ds.pixel_array)

                numpydata = asarray(im)
                channels2=len(numpydata.shape)
                print(str(channels2)+"pilo")
                
                depth=ds.pixel_array.dtype
    ########################################################
                depth2=dsInfo.BitsStored
                maxval=ds.pixel_array.max()
                minval=ds.pixel_array.min()
                print(maxval)
                print("inbetween")
                print(minval)
                # for i in range(len(ds.pixel_array)):
                #     ds.pixel_array[i]=((maxval-ds.pixel_array[i])/(maxval-minval))*255
                array1=((ds.pixel_array-minval)/(maxval-minval))*255
                maxval1=ds.pixel_array.max()
                minval1=ds.pixel_array.min()
                print(maxval1)
                print("inbetween")
                print(minval1)
    ############################################################
                self.show()

                self.ax1.imshow(array1, cmap='gray') 
                self.fig.canvas.draw()
                self.fig.canvas.flush_events()
                self.ax1.get_xaxis().set_visible(False)
                self.ax1.get_yaxis().set_visible(False)
                self.ax1.axis("off")
               
                try:
                    self.INFO1=dsInfo.PatientName
                except:
                    self.INFO1="not Avialabe"
                try:
                    self.INFO2=dsInfo.PatientAge
                except:
                    self.INFO2="not Avialabe"
                try:
                    self.INFO3=dsInfo.Modality
                except:
                    self.INFO3="not Avialabe"
                try:
                    self.INFO4=dsInfo.BodyPartExamined
                except:
                    self.INFO4="not Avialabe"
              
                self.Info.setText("Name :"+str(self.INFO1)+" \n AGE: "+str(self.INFO2)+"\n Modality: "+str(self.INFO3)+"\n PartExamined: "+str(self.INFO4)+",\n Size: "+str(dsInfo.__sizeof__()) +"\n width:"+str(im.width)+"\n height:" +str(im.height)+"\n depth: "+str(depth2)+ "\n Size: "+str(os.stat(FileName[0]).st_size*8)+"bit "+"\n Colors :Grey" )
               
            except:
                self.msg.setText("That DCM Image is corrupted!")
                self.msg.exec_()
        ####
        elif(file_extension=='.jpg' or file_extension=='.bmp' or file_extension=='.png' ):
            try:
                self.Bool=0
                # self.fig.set_visible(False)
                # self.fig.canvas.draw()
                self.fig.canvas.close()
                self.OutputImage.clear()
                # ###################
                # white = np.ones([50,50,3],dtype=np.uint8)
                # white[:] = 255
                # for i in range (4) :
                #     L=len(white[0])
                #     white[1][len(white)-i-1]=(200,0,0)
                #     white[L-i-1][1]=(0,0,200)
                # plt.imshow(white, cmap='gray')       
                # plt.show()
                ###############################
               
                ##################
                self.pixmap=QPixmap(FileName[0])
                im = Image.open(FileName[0])
               
                numpydata = asarray(im)
                channels2=len(numpydata.shape)
                print(str(channels2)+"pilo")
                depth=numpydata.dtype
                H=self.OutputImage.height()
                w=self.OutputImage.width()
                self.pix1=self.pixmap.scaled(H,w,QtCore.Qt.KeepAspectRatio)
                ####
                size=os.stat(FileName[0]).st_size*8
                bitsnum=len(im.tobytes())*8
                pixels=im.width*im.height
                
                depthreal=bitsnum/pixels
                self.OutputImage.setPixmap(self.pix1)
                if(channels2==3):
                    InfoColor="RGB"
                else:
                    InfoColor="Grey Scaled"
                if(depth!="bool"):
                    self.Info.setText("width:"+str(im.width)+"\n height:" +str(im.height)+"\n depth:"+str(depthreal)+ "\nSize:"+str(os.stat(FileName[0]).st_size*8)+"bit "+"\nColors " +str(InfoColor)  )
                else:
                    self.Info.setText("width:"+str(im.width)+" \n height:" +str(im.height)+" \n depth: =1"+ "\n Size: "+str(os.stat(FileName[0]).st_size*8)+"bit "+"\n Colors " +"Binary Scaled"  )
            except:
                self.msg.setText("That  Image is corrupted!")
                self.msg.exec_()
        else:
            self.msg.setText("Please Pick an Image!")
            self.msg.exec_()




    def Generate(self):
        self.lay2.addWidget(self.plotWidget2)

        self.fig2.canvas.draw()
        white = np.ones([50,50,3],dtype=np.uint8)
        white[:] = 255
        self.ax2.imshow(white, cmap='gray')       
        self.fig2.canvas.draw()

        self.show()
        self.Bool2=0

    def ShowPixels(self):
        if self.Bool2==1:

           self.msg.setText("click on generate first")
           self.msg.exec_()

        white = np.ones([50,50,3],dtype=np.uint8)
        white[:] = 255
        for i in range (4) :
            L=len(white[0])
            white[1][len(white)-i-1]=(200,0,0)
            white[L-i-1][1]=(0,0,200)
        self.fig2.canvas.draw()
        self.ax2.imshow(white, cmap='gray')       
        self.fig2.canvas.draw()

        self.show()



def main():
    
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()