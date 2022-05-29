from PyQt5 import QtWidgets,QtGui,QtCore
from matplotlib.colors import Normalize
from numpy.core.fromnumeric import shape
from numpy.fft.helper import ifftshift
from GuiT5 import Ui_MainWindow
import sys
from PyQt5.QtGui import *
from PIL import Image,ImageColor,ExifTags
import os
import matplotlib
from numpy import asarray, uint8
import cv2
import matplotlib.pyplot as plt
import pyqtgraph as pg
import pydicom
matplotlib.use('Qt5Agg')
import matplotlib.animation as animation
from pydicom.data import get_testdata_files
from PyQt5.QtWidgets import QFrame, QMainWindow, QMessageBox,QDesktopWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as Navi
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import struct
from matplotlib.figure import Figure
import numpy as np
from math import sqrt, floor, ceil
import math
from scipy.fftpack import fft2,ifft2,fftshift
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.center()
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
        self.filename='none'
        self.KNNBTN=self.ui.KNNBtn
        self.BilinearBTN=self.ui.BilinearBtn
        self.ZoomOutput=self.ui.ZoomLabel
        self.KNNBTN.clicked.connect(self.showKNN)
        self.GrayScaled=[]
        self.fig3,self.ax3 = plt.subplots(1,1)
        self.lay3=QtWidgets.QVBoxLayout(self.ZoomOutput)
        self.plotWidget3=FigureCanvas(self.fig3)
        self.lay3.addWidget(self.plotWidget3)
        # self.ax3.axis([0,1000,500,0])

        self.ZoomFactorInput=self.ui.ZoomFactor
        self.BilinearBTN.clicked.connect(self.ShowBilinear)
        self.fix_img=0
        self.EqualizeHistogramBtn=self.ui.EqualizeHBtn
        self.EqualizedImage=self.ui.EqualizedImage
        self.NormalizedHistoGram=self.ui.NormalizedH
        self.NormalizationOfEqualized=self.ui.EqaulizedH_N
        self.imageUsedInNormalization=[]
        
        self.EqualizeHistogramBtn.clicked.connect(self.EqualizedHistogram)
        self.fig4,self.ax4 = plt.subplots(1,1)
        self.lay4=QtWidgets.QVBoxLayout(self.NormalizedHistoGram)
        self.plotWidget4=FigureCanvas(self.fig4)
        self.lay4.addWidget(self.plotWidget4)
        self.fig5,self.ax5 = plt.subplots(1,1)
        self.lay5=QtWidgets.QVBoxLayout(self.NormalizationOfEqualized)
        self.plotWidget5=FigureCanvas(self.fig5)
        self.lay5.addWidget(self.plotWidget5)
        self.fig6,self.ax6 = plt.subplots(1,1)
        self.lay6=QtWidgets.QVBoxLayout(self.EqualizedImage)
        self.plotWidget6=FigureCanvas(self.fig6)
        self.lay6.addWidget(self.plotWidget6)
        self.Histogram=[]
        self.im=[]

        self.Image_Enahnced=self.ui.Image_Enahnced
        self.figEnhanced,self.axEnhanced = plt.subplots(1,1)
        self.figEnhanced.subplots_adjust(left=0,bottom=0,right=1,top=1,wspace=None,hspace=None)
        self.layEnhanced=QtWidgets.QVBoxLayout(self.Image_Enahnced)
        self.BoolEnhanced=0
        self.KernelSize=self.ui.KernelSize
        self.EnhanceFactor=self.ui.FactorValue
        self.EnhanceBtn=self.ui.Enhance_BTN
        self.EnhanceBtn.clicked.connect(self.convolve2D)
        self.Magnitude=self.ui.Magnitude
        self.phase=self.ui.Phase
        self.Image_FourierTab=self.ui.Image_FourierTab
        self.figMagnitude,self.axMagnitude = plt.subplots(1,1)
        self.layMagnitude=QtWidgets.QVBoxLayout(self.Magnitude)
        self.plotWidgetMagnitude=FigureCanvas(self.figMagnitude)
        self.layMagnitude.addWidget(self.plotWidgetMagnitude)
        self.figPhase,self.axPhase = plt.subplots(1,1)
        self.layPhase=QtWidgets.QVBoxLayout(self.phase)
        self.plotWidgetPhase=FigureCanvas(self.figPhase)
        self.layPhase.addWidget(self.plotWidgetPhase)
        self.figImgFourierTab,self.axImgFourierTab = plt.subplots(1,1)
        self.layImgFourierTab=QtWidgets.QVBoxLayout(self.Image_FourierTab)
        self.plotWidgetImgFourierTab=FigureCanvas(self.figImgFourierTab)
        self.layImgFourierTab.addWidget(self.plotWidgetImgFourierTab)
        self.FourierBtn=self.ui.Fourier
        self.FourierBtn.clicked.connect(self.Fourier)
        # self.figMagnitude.subplots_adjust(left=0,bottom=0,right=1,top=1,wspace=None,hspace=None)
        # self.figPhase.subplots_adjust(left=0,bottom=0,right=1,top=1,wspace=None,hspace=None)
        # self.figImgFourierTab.subplots_adjust(left=0,bottom=0,right=1,top=1,wspace=None,hspace=None)

    def Browse(self):
        FileName=QtWidgets.QFileDialog.getOpenFileName(self,"Open File","E:\\Year3 Term1\\Image Processing\\Task4","All Files (*);;PNG Files (*.png);;Tif Files (*.tif);;Jpg Files(*.jpg);; Bmp Files(*.bmp)")
        self.filename=FileName
        filename, file_extension = os.path.splitext(FileName[0])
        
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
        elif(file_extension=='.jpg' or file_extension=='.bmp' or file_extension=='.png'  or file_extension=='.jpeg' ):
            # try:
                # self.Bool=0
                # self.fig.set_visible(False)
                # self.fig.canvas.draw()
                # self.fig.canvas.close()
                # self.OutputImage.clear()
                # ###################
              
                if self.Bool==0:
                    self.plotWidget=FigureCanvas(self.fig)
                self.Bool=1             
                self.lay.addWidget(self.plotWidget)

                self.pixmap=QPixmap(FileName[0])
                im = Image.open(FileName[0])
                pixels=im.width*im.height



                #task3#####################################################
                # self.GaussianBlurImage(im,4)
                self.im=im
                im = im.convert("L")  #Convert photo to gray scale
                im = np.asarray(im)   #Convert variable type to numpy array
                
                self.imageUsedInNormalization=im

                
               
                ############################################################
                img = cv2.imread(FileName[0])
                fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.fix_img=fix_img
                R, G, B = fix_img[:,:,0], fix_img[:,:,1],fix_img[:,:,2]
                Y = 0.299 * R + 0.587 * G + 0.114 * B
                self.fig.canvas.draw()
                self.ax1.get_xaxis().set_visible(False)
                self.ax1.get_yaxis().set_visible(False)
                self.ax1.axis("off")   
                self.ax1.imshow(Y, cmap='gray')
                        
                self.show()
                self.GrayScaled=Y


                self.fig.canvas.draw()
######################################
                numpydata = asarray(im)
                channels2=len(numpydata.shape)
                depth=numpydata.dtype
                H=self.OutputImage.height()
                w=self.OutputImage.width()
                self.pix1=self.pixmap.scaled(H,w,QtCore.Qt.KeepAspectRatio)
                ####
                size=os.stat(FileName[0]).st_size*8
                bitsnum=len(im.tobytes())*8
                
                depthreal=bitsnum/pixels
                # # self.OutputImage.setPixmap(self.pix1)
                # if(channels2==3):
                #     InfoColor="RGB"
                # else:
                #     InfoColor="Grey Scaled"
                # if(depth!="bool"):
                #     self.Info.setText("width:"+str(im.width)+"\nheight:" +str(im.height)+"\ndepth:"+str(depthreal)+ "\nSize:"+str(os.stat(FileName[0]).st_size*8)+"bit "+"\nColors " +str(InfoColor)  )
                # else:
                #     self.Info.setText("width:"+str(im.width)+" \nheight:" +str(im.height)+" \ndepth: =1"+ "\nSize: "+str(os.stat(FileName[0]).st_size*8)+"bit "+"\nColors " +"Binary Scaled"  )
            # except:
                # self.msg.setText("That  Image is corrupted!")
                # self.msg.exec_()
        else:
            self.msg.setText("Please Pick an Image!")
            self.msg.exec_()
    


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def DrawFourierTab(self,Image,Magnitude,Phase):
        self.axMagnitude.get_xaxis().set_visible(False)
        self.axMagnitude.get_yaxis().set_visible(False)
        self.axMagnitude.axis("off")
        self.axPhase.get_xaxis().set_visible(False)
        self.axPhase.get_yaxis().set_visible(False)
        self.axPhase.axis("off")
        self.axImgFourierTab.get_xaxis().set_visible(False)
        self.axImgFourierTab.get_yaxis().set_visible(False)
        self.axImgFourierTab.axis("off")
               
        Image=self.GrayScaled
        self.figImgFourierTab.canvas.draw()
        self.figImgFourierTab.canvas.draw()
        self.axImgFourierTab.imshow(Image,cmap='gray')
        self.figImgFourierTab.canvas.draw()

        self.show()
        self.axMagnitude.imshow(Magnitude,cmap='gray')
        self.show()

        self.figMagnitude.canvas.draw()
        self.axPhase.imshow(Phase,cmap='gray')
        self.show()

        self.figPhase.canvas.draw()

    def Fourier(self):
        img=np.asarray(self.GrayScaled)
        dft=fft2(img)#2D fourier transform for the image
        dft=fftshift(dft)
        real=dft.real
        imaginary=dft.imag
        phase=np.arctan(imaginary/real)
        real=dft.real
        imaginary=dft.imag
        addition=real**2+imaginary**2
        squareroot=np.sqrt(addition)
        dft=squareroot
        magnitude=dft
        print(magnitude)
       
        # for i in range(len(magnitude)):
        #     if (magnitude[i]>200).any():
        #         magnitude[i]=0
        # realnew=magnitude**2-imaginary**2
        # realnew=np.sqrt(realnew)
        # NewFourier=realnew+1J*imaginary
        # ImagNew=ifftshift(NewFourier)

        # ImagNew=ifft2(ImagNew)
        # ImageFinished=np.abs(ImagNew) 

        # # c = 255 / np.log(1 + np.max(ImageFinished))
        # # ImageFinished = c * np.log (1 + ImageFinished)

        # ImageFinished=np.asarray(ImageFinished)
        # ImageFinished=(ImageFinished).astype(uint8)
        # print(ImageFinished)


        # # ImageFinished=((ImageFinished-ImageFinished.max())/(ImageFinished.max()-ImageFinished.min()))*255
        # # ImagNew=np.asarray(ImagNew)
        # # ImagNew=ImagNew*15
        

        # plt.imshow(ImageFinished,cmap='gray',vmin=0,vmax=255)
        # plt.show()
        
        magnitude=np.float32(dft)
        
        c = 255 / np.log(1 + np.max(magnitude))
        magnitude = c * np.log (1 + magnitude)
        magnitude=np.asarray(magnitude)
      

        self.axPhase.clear()
        self.axMagnitude.clear()
        self.DrawFourierTab(img,magnitude,phase)
        

   

    def convolve2D(self, padding=1):
        try:
            if self.Bool==0:
                self.msg.setText("Browse first")
                self.msg.exec_()
            else:
                image=self.GrayScaled
                Factor=float(self.EnhanceFactor.text())
                kernelsize=int(self.KernelSize.text())
                    
                print(kernelsize)
                if Factor <=0.0 or kernelsize%2==0 or kernelsize==1:
                    self.msg.setText("kernel size must be odd and greater than 1 and Factor cannot be neagtive")
                    self.msg.exec_()
                else:
                    count=1
                    for i in range (2,kernelsize):
                        if(i%2!=0):
                            count+=1
                    padding=count
                    if self.BoolEnhanced==0:
                        self.plotWidgetEnhanced=FigureCanvas(self.figEnhanced)
                    self.BoolEnhanced=1
                    self.axEnhanced.get_xaxis().set_visible(False)
                    self.axEnhanced.get_yaxis().set_visible(False)
                    self.axEnhanced.axis("off")   
                    self.layEnhanced.addWidget(self.plotWidgetEnhanced)
                    mag=kernelsize*kernelsize
                    kernel = np.ones((kernelsize, kernelsize))
                    kernel=kernel*1/mag

                    xKernShape = kernel.shape[0]
                    yKernShape = kernel.shape[1]
                    xImgShape = image.shape[0]
                    yImgShape = image.shape[1]

                    xOutput = xImgShape
                    yOutput = yImgShape
                    output = np.zeros((xOutput, yOutput))

                    imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
                    imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
                

                    for y in range(image.shape[1]):
                      
                        for x in range(image.shape[0]):
                          
                            try:
                                output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                            except:
                
                                break
                
                    sharpen=image-output
                    
                    output=image+Factor*sharpen
                    for j in range(0,output.shape[0]):
                        for i in range(0,output.shape[1]):
                            if output[j,i]>255 :
                                output[j,i]=255
                            elif output[j,i]<0:
                                output[j,i]=0
                
                    self.figEnhanced.canvas.draw()
                    self.axEnhanced.imshow(output,cmap='gray')
                    self.show()
                    self.figEnhanced.canvas.draw()

                    return output
        except:
            self.msg.setText("Enter Factor and kernel size first ")
            self.msg.exec_()
    def EqualizedHistogram(self):
        try:
            self.fig6.canvas.draw()
            im=self.GrayScaled

            h=self.NormalizeHistogram(im,2)
            im=np.asarray(im)
            im=np.round(im)
            im=im.astype(int)
            
            b=[sum(h[:i+1]) for i in range(len(h))]

            cumulative=np.array(b)
            cumsum=np.round(cumulative*255)
            cumsum=cumsum.astype(int)
            s1,s2=im.shape
            
            NewIM = np.zeros_like(im)
            for i in range(0, s1):
                for j in range(0, s2):
                    NewIM[i, j] =  cumsum[im[i, j]]
        
            self.ax6.imshow(NewIM,cmap='gray')
            
            self.show()
            self.fig6.canvas.draw()
            NewIM=np.uint8(NewIM)
            self.NormalizeHistogram(NewIM,1)
        except:
            self.msg.setText("browse first")
            self.msg.exec_()
    def Draw(self,normalizedH,I,r,EqN):
     
        self.fig4.canvas.draw()
        self.fig4.canvas.draw()
       
        self.ax4.bar(r,normalizedH)
        self.show()
        self.ax5.bar(r,EqN)
        self.show()
        self.fig5.canvas.draw()
    def NormalizeHistogram(self,GrayScaled,n):
        r=[]
        im=GrayScaled
        im=np.asarray(im)
        im=np.round(im)
        im=im.astype(int)
        h = [0]*256  
        for x in range(im.shape[0]):        
            for y in range(im.shape[1]):            
                i = round(im[x,y])   
                #specfic intensity
                if i<=256:
                    h[i] = h[i]+1     #had 1 of a specfic intensity then add one and repeat
                else:
                    pass
        for i in range (len(h)):
            r.append(i)
        newh=np.asanyarray(h)
        normalizedH=newh/(im.shape[0]*im.shape[1])
        if n==0:
            self.ax4.clear()
            self.Draw(normalizedH,0,r,0)
        elif n==1:
            self.ax5.clear()
            self.Draw(0,0,r,normalizedH)
    
        return h
      
    def showKNN(self):

        try:
            self.ax3.clear()
            Factor=float(self.ZoomFactorInput.text())
            print(Factor)

            if Factor <=0.0 :
                self.msg.setText("you cannot put zero or negative")
                self.msg.exec_()
               
            else:
                self.fig3.canvas.draw()
                newwidth=int(Factor*self.Y.shape[0])
                newheight=int(Factor*self.Y.shape[1])
                zoomed=np.zeros((newwidth,newheight),dtype=self.Y.dtype)
                for i in range(0,newwidth):
                    for j in range(0, newheight):
                        if i/Factor>self.Y.shape[0]-1 or j/Factor>self.Y.shape[1]-1:
                            zoomed[i,j]=self.Y[int(i/Factor),int(j/Factor)]
                        else:
                            zoomed[i,j]=self.Y[round(i/Factor),round(j/Factor)]
                self.ax3.axis([0,1200,600,0])

                self.ax3.imshow(zoomed,cmap='gray')
                self.fig3.canvas.draw()

                self.show()
        except:
            self.msg.setText("browse first then put a zooming factor\n make sure zooming factor is a postive number only")
            self.msg.exec_()

    def ShowBilinear(self):
        try:
            self.ax3.clear()

            Factor=float(self.ZoomFactorInput.text())
            if Factor <=0.0 :
                self.msg.setText("you cannot put zero or negative")
                self.msg.exec_()
            else:
                self.fig3.canvas.draw()

                newwidth=int(Factor*self.Y.shape[0])
                newheight=int(Factor*self.Y.shape[1])
                # # ##################################################################
                #get dimensions of original image
                old_h, old_w, c = self.fix_img.shape
                #create an array of the desired shape. 
                #We will fill-in the values later.
                resized = np.zeros((newheight, newwidth, c))
                #Calculate horizontal and vertical scaling factor
                w_scale_factor = (old_w ) / (newwidth ) if newheight != 0 else 0
                h_scale_factor = (old_h ) / (newheight ) if newwidth != 0 else 0
                for i in range(newheight):
                    for j in range(newwidth):
                        #map the coordinates back to the original image
                        x = i * h_scale_factor
                        y = j * w_scale_factor
                        #calculate the coordinate values for 4 surrounding pixels.
                        x_floor = math.floor(x)
                        x_ceil = min( old_h - 1, math.ceil(x))
                        y_floor = math.floor(y)
                        y_ceil = min(old_w - 1, math.ceil(y))
                # case 1 it has specfic pixel in old image so we assign it 
                        if (x_ceil == x_floor) and (y_ceil == y_floor): 
                            q = self.fix_img[int(x), int(y), :]
        #when one of them is specfic we do linear interpolation for one only
                        elif (x_ceil == x_floor):
                            q1 = self.fix_img[int(x), int(y_floor), :]
                            q2 = self.fix_img[int(x), int(y_ceil), :]
                            q = q1 * (y_ceil - y) + q2 * (y - y_floor)
                        elif (y_ceil == y_floor):
                            q1 = self.fix_img[int(x_floor), int(y), :]
                            q2 = self.fix_img[int(x_ceil), int(y), :]
                            q = (q1 * (x_ceil - x)) + (q2	 * (x - x_floor))
                        else:
                            v1 = self.fix_img[x_floor, y_floor, :]
                            v2 = self.fix_img[x_ceil, y_floor, :]
                            v3 = self.fix_img[x_floor, y_ceil, :]
                            v4 = self.fix_img[x_ceil, y_ceil, :]

                            q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
                            q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
                            q = q1 * (y_ceil - y) + q2 * (y - y_floor)

                        resized[i,j,:] = q
                R2, G2, B2= resized[:,:,0], resized[:,:,1],resized[:,:,2]
                self.ax3.axis([0,1200,600,0])

                Y2 = 0.299 * R2 + 0.587 * G2 + 0.114 * B2
                self.ax3.imshow(Y2,cmap='gray')
                self.fig3.canvas.draw()

                self.show()
        except:
            self.msg.setText("browse first then put a zooming factor\n make sure zooming factor is number only")
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