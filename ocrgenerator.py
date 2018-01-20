#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
#pickedrectangleselector
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import matplotlib.patches
import matplotlib.widgets as widgets
from matplotlib.widgets import RectangleSelector
import sys
from matplotlib.patches import Rectangle
import matplotlib
from matplotlib.widgets import Button
#layoutanalyser
import cv2
import sajhead
#ocr
import lekha_work as ocr

myendcordinates=[]
overalapchecker=[]
imgloc=0

class ProgressBarWindow():
    def __init__(self):
        self.progresswindow = builder.get_object("progressbar_window")
        self.progresswindow.set_transient_for(window)
        self.progresswindow.show_all()

class LayoutAnalysedfigure():
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.point = self.ax.plot([],[], marker="o", color="crimson")
        #clear button     
        self.axclear = plt.axes([0.3, 0.01, 0.09,0.06])
        self.bnclear = Button(self.axclear, 'Clear All')
        self.bnclear.color = "orange"
        #undo button
        self.axundo = plt.axes([0.4, 0.01, 0.09,0.06])
        self.bnundo = Button(self.axundo, 'UNDO')
        self.bnundo.color = "red"
        #proceedbutton
        self.axproceed = plt.axes([0.5, 0.01, 0.095, 0.06])
        self.bnproceed = Button(self.axproceed, 'PROCEED')
        self.bnproceed.color = "green"
        #usage 1
        self.usg1 =plt.figtext(0.26, 0.96, 'PRESS "ENTER" AFTER SELECTING TO CONFIRM THE SELECTION')
        self.usg1.set_color('brown')
        self.usg1.set_weight('bold')
        #usage 2
        self.usg2 = plt.figtext(0.3, 0.93, 'CLICK ON THE DRAWN RECTANGLES TO DELETE IT')
        self.usg2.set_color('brown')
        self.usg2.set_weight('bold')

        self.rect = [] 
        self.rs = RectangleSelector(self.ax,self.line_select_callback,
                       drawtype='box', useblit=False, button=[1], 
                       minspanx=2, minspany=2, spancoords='pixels', 
                       interactive=True)

    def checkoverlap(self,l1x,l1y,r1x,r1y,l2x,l2y,r2x,r2y):
      #checking overlap
            
        # If one rectangle is on left side of other
        if l1x > r2x or l2x > r1x :
            print("i am printing in first if condition")
            return False
     
        #If one rectangle is above other
        if l1y > r2y or l2y > r1y :
            print("i am printing in second if condition")
            return False    
        return True


    def line_select_callback(self,eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        rid = self.fig.canvas.mpl_connect('button_press_event', lambda event: self.outsideclick(event,cid))
        cid = self.fig.canvas.mpl_connect('key_press_event', lambda event: self.press(event,x1,y1,x2,y2,cid))
        #if it is inside already drawn rectangles
        l2x = x1 
        l2y = y1
        r2x = x2
        r2y = y2
        count =len(overalapchecker)
        
        i = 0
        while i < count:
            l1x = overalapchecker[i][0]
            l1y = overalapchecker[i][1]
            r1x = overalapchecker[i][2]
            r1y = overalapchecker[i][3]
            print(l1x,l1y,r1x,r1y)
            ovrlap = self.checkoverlap(l1x,l1y,r1x,r1y,l2x,l2y,r2x,r2y)
            print(ovrlap)  
            if(ovrlap) :
                print(ovrlap)
                print(cid)     
                self.rs.to_draw.set_visible(False)
                self.fig.canvas.mpl_disconnect(cid)
               
                  
          
       
            i = i +1 
            
       
       


    def press(self,event,x1,y1,x2,y2,cid):
        print('press', event.key)
       # print (x1,y1,x2,y2,cid)
        sys.stdout.flush()
        if event.key == 'enter':
            print("Enter Key pressed")
            print("current selection box id=",cid)
            width = x2-x1
            height = y2-y1
            print(width,height)
            myendcordinates.append((x1,y1,width,height))
            overalapchecker.append((x1,y1,x2,y2))
            print(myendcordinates)
            

            #print(myendcordinates)
            
            self.rect.append(plt.Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2),fill =False,picker=True))
            self.ax.add_patch(self.rect[-1])
            #self.fig.canvas.mpl_connect('key_press_event', lambda event: self.deletepress(event,rect,cid))
            print(self.rect[-1])
           
           

    def outsideclick(self,event,cid):
      #  print(event.xdata,event.ydata)
        print("disconnecting",cid)
       # plt.disconnect(cid)
        self.fig.canvas.mpl_disconnect(cid)     
        
   

            

    def onpick1(self,event):
       
        if isinstance(event.artist, Rectangle):
            patch = event.artist
            height=patch.get_height()
            #rectevent = event
          #  patch.remove()
            print('onpick1 patch:', patch.get_path())
            print("heigth=",height)
            patch.get_path()
            dx1 = patch.get_x()
            dy1 = patch.get_y()
            dh1 = patch.get_height()
            dw1 = patch.get_width() 
            dx2 = dx1 + dw1
            dy2 = dy1 + dh1 
            patch.get_path()
            # patch.set_visible(False)
            patch.remove()
            print(len(self.rect))
            print(patch)
            
            if patch in self.rect :
                print("yes present")
                self.rect.remove(patch)
                myendcordinates.remove((dx1,dy1,dw1,dh1))
                overalapchecker.remove((dx1,dy1,dx2,dy2))
                print('rectangle removed')
            else :
                print ("%s not present" %(patch)) 

            
            print(len(self.rect))
            #print(patch)
           

            # matplotlib.axes.Axes.relim(self)
          
           
            for i, e in reversed(list(enumerate(self.rect))):
                print(i, e)
            #print(myendcordinates)
           
            #print(dx1,dy1,dx2,dy2)
            #remrect = Rectangle( (min(dx1,dx2),min(dy1,dy2)), np.abs(dx1-dx2), np.abs(dy1-dy2))
            #dwx =int(min(dx1,dx2))
            #dwy =int(min(dy,dy2))

           # print(dwr) 
          #  print(remrect)
                 
            print(len(self.rect))
             
        

   
   
    def boxundoing(self,event):
        #print(self.rect)
      
        #print(self.rect[-1])
        self.rect[-1].set_visible(False)
        self.rect.pop() 
        #n = len(self.rect)
        #print(n)
        #for i, e in reversed(list(enumerate(self.rect))):
        #    if e.get_visible() == True :
        #        print(i, e)
        #        print(e.get_visible())
        #        e.set_visible(False)
        #        print(e.get_visible())
        #        break
        myendcordinates.pop()
        n = len(self.rect)
        print(n)
        p = len(myendcordinates)
        print("length of myendcordinates = %d" %(p))
        overalapchecker.pop()
        q= len(overalapchecker)
        print("length of myendcordinates = %d" %(q))
        print(myendcordinates)
        for i, e in reversed(list(enumerate(self.rect))):
            print(i, e)

    def boxclearing(self,event):
        
       # self.rect[-1].set_visible(False)
       # self.rect.pop() 
        #n = len(self.rect)
        #print(n)
        for i, e in reversed(list(enumerate(self.rect))):
            e.set_visible(False)
           
        myendcordinates.clear()
        self.rect.clear()
        n = len(self.rect)
        print(n)
        p = len(myendcordinates)
        print("length of myendcordinates = %d" %(p))
        overalapchecker.clear()
        q= len(overalapchecker)
        print("length of myendcordinates = %d" %(q))
        print(myendcordinates)
        for i, e in reversed(list(enumerate(self.rect))):
            print(i, e)
    
    def proceedtoocr(self,event):
        #do cutting image and calling ocr one by one later
        outputstring =''
        plt.close('all')
        #progressw =  ProgressBarWindow()    
        img = cv2.imread(imgloc,0)
        print(len(myendcordinates))
        for c in myendcordinates:
           #print(c[0])
           # print(c[1])
           # print(c[2])
           # print(c[3])
            x = int(c[0])
            y = int(c[1])
            h = int(c[3])
            w = int(c[2])
            crop_img = img[y:y+h, x:x+w]
            text = ocr.lekha_run(crop_img)
            filename = str(c[0]) + ".jpg"
            cv2.imwrite(filename,crop_img)
            strtext = str(text)
            outputstring = outputstring + "\n" + strtext
            #print(strtext)
        textview = builder.get_object("outputtextview")
        textview.get_buffer().set_text(outputstring)
        f = open('test.txt', 'w')
        f.write(outputstring)
        f.close()



#handler class
class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def on_about(self, widget):
        about_dialog = builder.get_object("about_window")
        about_dialog.show()
    

    def closewindow(self, arg1, arg2):
        about_dialog = builder.get_object("about_window")
        about_dialog.hide()
        return True



    def addimagebuttonclicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", None,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            global imgloc
            imgloc = dialog.get_filename()
            sw = builder.get_object("scrolled_window")   
            window = builder.get_object("main_window")
            
            #clear the text area
            textviewinitial = builder.get_object("outputtextview")
            textviewinitial.get_buffer().set_text('')

            img = builder.get_object("previmage")
            img.set_from_file(imgloc)
            #sw.add(img)


        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_img = Gtk.FileFilter()
        filter_img.set_name("Image files")
        filter_img.add_mime_type("image/jpeg")
        filter_img.add_mime_type("image/jpg")
        filter_img.add_mime_type("image/png")
        filter_img.add_mime_type("image/bmp")
        filter_img.add_mime_type("image/tiff")
        dialog.add_filter(filter_img)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
    
  

    def scan_button_clicked_cb(self, widget):
        os.system("simple-scan")

    def generate_button_clicked(self,widget):
        overalapchecker.clear()
        myendcordinates.clear()
        figureobject = LayoutAnalysedfigure()
        im = cv2.imread(imgloc,0)
        #a= sajhead.head(im)
        h,b=sajhead.boundary(im.copy())
        a = h + b 
        print(a)
        imgep = builder.get_object("previmage")
        print(imgloc)
        #img = np.array(Image.open('/home/space-kerala/Downloads/test1.png'), dtype=np.uint8)
        img = np.array(Image.open(imgloc), dtype=np.uint8)
        
        figureobject.ax.imshow(img, aspect = 'equal',extent = None)

        #print (a)
        #print(a[0][0])
        for r in a:
            #print (r)
            #print (r[0])
            lx1 = r[0]
            ly1 = r[1]
            lx2 = r[0] + r[2]
            ly2 = r[1] + r[3]
            figureobject.rect.append(plt.Rectangle( (min(lx1,lx2),min(ly1,ly2)), np.abs(lx1-lx2), np.abs(ly1-ly2),fill =False,picker=True))
            figureobject.ax.add_patch(figureobject.rect[-1])
            myendcordinates.append((lx1,ly1,r[2],r[3]))
            overalapchecker.append((lx1,ly1,lx2,ly2))
            
        figureobject.fig.canvas.mpl_connect('pick_event', figureobject.onpick1)
        figureobject.bnundo.on_clicked(figureobject.boxundoing)
        figureobject.bnclear.on_clicked(figureobject.boxclearing)
        figureobject.bnproceed.on_clicked(figureobject.proceedtoocr)
        plt.show() 
         
            


        
   
   
 



builder = Gtk.Builder()
builder.add_from_file("ocrgeneratorui.glade")
builder.connect_signals(Handler())





window = builder.get_object("main_window")
window.set_icon_from_file('icon.png')
window.show_all()

Gtk.main()

#allcommentsforreference

#print(cid)
#print(cid)
#rect = plt.Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2),fill =False )
#ax.add_patch(rect)
#patch.relim()
#print(overalapchecker) 
#def onclick(self,event,patch,connection_id):
       # if event.dblclick:
       #     patch =event.artist
          #  print('double clicked')
         #   print(patch)
       #     patch.get_path()
       #     dx1 = patch.get_x()
       #     dy1 = patch.get_y()
       #     dh1 = patch.get_height()
       #     dw1 = patch.get_width() 
       #     patch.get_path()
       #     # patch.set_visible(False)
       #     print(dx1,dy1,dw1,dh1)
       #     patch.remove()
            # matplotlib.axes.Axes.relim(self)
       #     print('rectangle removed')
       #     myendcordinates.remove((dx1,dy1,dw1,dh1))
       #     print(myendcordinates)
       #     dx2 = dx1 + dw1
       #     dy2 = dy1 + dh1 
       #     overalapchecker.remove((dx1,dy1,dx2,dy2))
       #     self.fig.canvas.mpl_disconnect(connection_id) 
        #def deletepress(self,event,rect,cid):
     #   if event.key == 'delete':    
      #      self.rect.set_visible(False)  
       #     myendcordinates.clear()
       #     overalapchecker.clear()
        #    print(myendcordinates)

           

    #def callback(event):
      #  print (event.xdata, event.ydata)


    #plt.disconnect(cid)
    #fig.canvas.callbacks.connect('button_press_event', callback)
  #  def onpickrect(self,event):
       
  #      if isinstance(event.artist, Rectangle):
  #          print("hey you are inside a rectangle")

          #  rect.set_visible(False)  

       # elif event.key != 'enter':    
       #        print("disconnecting id=",cid) 
       #        plt.disconnect(cid)               
#clearbuttonpassingdataclass
#class ButtonDataProcessor(object):
  #  def __init__(self,bnclear,rect):
   #     self.rect =rect
    #    bnclear.on_clicked(self.process)
       # connection_id = fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event,patch,connection_id))   
            