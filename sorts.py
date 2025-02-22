from PyQt6 import QtCore

class SortAlgo(QtCore.QThread):
    def __init__(self,parent=None,graphArray=None,speed=1):
        QtCore.QThread.__init__(self,parent)
        self.graphArray=graphArray
        self.speed=int(100/speed)
        
    def swap(self,i,j):
        tmp=self.graphArray.array[i]
        self.graphArray.array[i]=self.graphArray.array[j]
        self.graphArray.array[j]=tmp
        
    def pivoting(self,aPivot,begin,end):
        pivot=self.graphArray.array[aPivot]
        self.graphArray.selected1=aPivot
        self.graphArray.selected2=begin
        self.graphArray.selected3=end-1
        while True:
            while self.graphArray.array[begin]<pivot:
                begin+=1
                self.graphArray.selected2+=1
            while self.graphArray.array[end-1]>pivot:
                end-=1
                self.graphArray.selected3-=1
            if begin>=end-1:
                return begin
            self.swap(begin,end-1)
            self.graphArray.update()
            self.msleep(self.speed)
            
    def merge(self,begin,end):
        halfSize=(end-begin)//2
        array1=self.graphArray.array[begin:begin+halfSize]
        array2=self.graphArray.array[begin+halfSize:end]
        ind1,ind2,ind=0,0,begin
        self.graphArray.selected1=begin
        while ind1<len(array1) or ind2<len(array2):
            if ind1==len(array1):
                self.graphArray.array[ind]=array2[ind2]
                ind2+=1
                self.graphArray.update()
                self.msleep(self.speed)
            elif ind2==len(array2):
                self.graphArray.array[ind]=array1[ind1]
                ind1+=1
                self.graphArray.update()
                self.msleep(self.speed)
            else:
                if array1[ind1]<=array2[ind2]:
                    self.graphArray.array[ind]=array1[ind1]
                    ind1+=1
                    self.graphArray.update()
                    self.msleep(self.speed)
                else:
                    self.graphArray.array[ind]=array2[ind2]
                    ind2+=1
                    self.graphArray.update()
                    self.msleep(self.speed)
            ind+=1
            self.graphArray.selected1+=1
            
    def bubbleSort(self):        
        for i in range(len(self.graphArray.array)-1):
            for j in range(len(self.graphArray.array)-1-i):
                if self.graphArray.array[j]>self.graphArray.array[j+1]:
                    self.swap(j,j+1)
                    self.graphArray.update()
                    self.msleep(self.speed)
                    
    def selectionSort(self):        
        for i in range(len(self.graphArray.array)):
            min=i
            self.graphArray.selected1=i
            self.graphArray.update()
            for j in range(i+1,len(self.graphArray.array)):
                if(self.graphArray.array[j]<self.graphArray.array[min]):
                    min=j
                    self.graphArray.selected1=j
                self.graphArray.selected2=j
                self.graphArray.update()               
                self.msleep(self.speed)                    
            self.swap(i,min)
                    
    def quickSort(self,begin,end):
        if end-begin==2:
            if self.graphArray.array[begin]>self.graphArray.array[end-1]:
                self.swap(begin,end-1)
                return
        if end-begin<=1:
            return
        pivot=(end-begin)//2
        pivot=self.pivoting(pivot+begin,begin,end)
        self.quickSort(begin,pivot)
        self.quickSort(pivot,end)        
        
    def mergeSort(self,begin,end):
        if(end-begin<=1):
            return
        halfSize=(end-begin)//2
        self.mergeSort(begin,begin+halfSize)
        self.mergeSort(begin+halfSize,end)
        self.merge(begin,end)
        
    def run(self):
        if self.graphArray!=None:
            match self.parent().sortsWidget.cbox.currentText():
                case "Пузырьком":
                    self.bubbleSort()
                case "Выбором":
                    self.selectionSort()
                case "Быстрая":
                    self.quickSort(0,len(self.graphArray.array))
                case "Слиянием":
                    self.mergeSort(0,len(self.graphArray.array))
                case _:
                    pass
        self.graphArray.selected1=-1
        self.graphArray.selected2=-1
        self.graphArray.selected3=-1
        self.graphArray.update()
        self.parent().elemsWidget.setEnabled(True)
        self.parent().actShuffle.setEnabled(True)
        self.parent().sortsWidget.setEnabled(True)
        self.parent().speedWidget.setEnabled(True)
        self.parent().actStart.setEnabled(True)
        self.parent().actStop.setEnabled(False)
        