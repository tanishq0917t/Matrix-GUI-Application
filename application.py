import tkinter
import tkinter.ttk
import tkinter.messagebox
class MyWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Tanishq Rawat-Matrix Calculator")
        self.geometry("900x400")
        self.resetList=[]
        self.operationLabel=tkinter.ttk.Label(self,text="Select operation to perform ")
        self.operationLabel.grid(row=0,column=0,sticky="W")
        self.operation=tkinter.ttk.Combobox(self,width=10,state='readonly')
        self.operation.grid(row=0,column=1,sticky="W",padx= 10,pady=5)
        self.operation["values"]=("Add","Subtract","Transpose","Multiply")
        self.generateButton=tkinter.ttk.Button(self,text="Generate",command=self.generateButtonHandler)
        self.generateButton.grid(row=0,column=2,padx= 10,pady=5)
        self.operateButton=tkinter.ttk.Button(self,text="Calculate",command=self.operateButtonHandler)
        self.operateButton.grid(row=0,column=3,padx= 10,pady=5)
        self.rowLabel=tkinter.ttk.Label(self,text="Enter number of rows of Matrix A")
        self.rowLabel.grid(row=1,column=0,sticky="W",pady=5)
        self.rowEntry=tkinter.ttk.Entry(self,width=5)
        self.rowEntry.grid(row=1,column=1,sticky="W",pady=5)
        self.columnLabel=tkinter.ttk.Label(self,text="Enter number of columns of Matrix A")
        self.columnLabel.grid(row=2,column=0,sticky="W",pady=5)
        self.columnEntry=tkinter.ttk.Entry(self,width=5)
        self.columnEntry.grid(row=2,column=1,sticky="W",pady=5)
        self.rowBLabel=tkinter.ttk.Label(self,text="Enter number of rows of Matrix B")
        self.rowBLabel.grid(row=3,column=0,sticky="W",pady=5)
        self.rowBEntry=tkinter.ttk.Entry(self,width=5)
        self.rowBEntry.grid(row=3,column=1,sticky="W",pady=5)

        self.columnBLabel=tkinter.ttk.Label(self,text="Enter number of columns of Matrix B")
        self.columnBLabel.grid(row=4,column=0,sticky="W",pady=5)
        self.columnBEntry=tkinter.ttk.Entry(self,width=5)
        self.columnBEntry.grid(row=4,column=1,sticky="W",pady=5)
        self.mulLabel=tkinter.ttk.Label(self,text="In Case of multiplication\nrows of A Matrix Should be\nequal to Columns of B Matrix\nOtherwise\nDimensions of A Matrix Should be\nequal to Dimensions of B Matrix\nIn case of Transpose\nDont fill Matrix B dimensions")
        self.mulLabel.grid(row=5,column=0)    
    def generateButtonHandler(self):
        rows=int(self.rowEntry.get())
        columns=int(self.columnEntry.get())
        if self.operation.get()=="Multiply":
            brows=int(self.rowBEntry.get())
            bcolumns=int(self.columnBEntry.get())
            if brows!=columns: return
        if self.operation.get()=="Add" or self.operation.get()=="Subtract":
            brows=int(self.rowBEntry.get())
            bcolumns=int(self.columnBEntry.get())
            if bcolumns!=columns or brows!=rows: return
        self.mulLabel.grid_remove()
        self.rowEntry.grid_remove()
        self.rowLabel.grid_remove()
        self.columnEntry.grid_remove()
        self.columnLabel.grid_remove()
        self.rowBEntry.grid_remove()
        self.rowBLabel.grid_remove()
        self.columnBEntry.grid_remove()
        self.columnBLabel.grid_remove()
        self.noteLabel=tkinter.ttk.Label(self,text="Note: Enter value of row as: 1 2 3",font=("Arial Bold",10))
        self.ALabel=tkinter.ttk.Label(self,text="Matrix A")
        self.ALabel.grid(row=1,column=0,pady=2)
        if self.operation.get()!="Transpose":
            self.BLabel=tkinter.ttk.Label(self,text="Matrix B")
            self.BLabel.grid(row=1,column=1,pady=2)
            self.resetList.append(self.BLabel)
            
        self.noteLabel.grid(row=0,column=4)
        self.resetList.append(self.ALabel)
        self.resetList.append(self.noteLabel)


        self.rowEntries=[]
        self.columnEntries=[]
        x=1
        if self.operation.get()!="Multiply":
            while x<=rows:
                entry1=tkinter.ttk.Entry(self,width=15)
                entry1.grid(row=x+2,column=0,pady=2)
                self.rowEntries.append(entry1)
                if self.operation.get()!="Transpose":
                    entry2=tkinter.ttk.Entry(self,width=15)
                    entry2.grid(row=x+2,column=1,pady=2)
                    self.columnEntries.append(entry2)
                x+=1
        else:
            while x<=rows:
                entry1=tkinter.ttk.Entry(self,width=15)
                entry1.grid(row=x+2,column=0,pady=2)
                self.rowEntries.append(entry1)
                x+=1
            x=1
            while x<=columns:
                entry2=tkinter.ttk.Entry(self,width=15)
                entry2.grid(row=x+2,column=1,pady=2)
                self.columnEntries.append(entry2)
                x+=1
        self.resetList.append(self.rowEntries)
        if self.operation.get()!="Transpose":
            self.resetList.append(self.columnEntries)

    def operateButtonHandler(self):
        if self.operation.get()=="Add":
            matrixA=[]
            matrixB=[]
            for row in self.rowEntries:
                matrixA.append(list(map(int,(row.get()).split())))
            for row in self.columnEntries:
                matrixB.append(list(map(int,(row.get()).split())))
            matrixC=[]
            lst=[]
            for i in range(len(matrixA)):  
                lst=[]
                for j in range(len(matrixA[0])):
                    lst.append(matrixA[i][j] + matrixB[i][j])
                matrixC.append(lst)
                
            self.CLabel=tkinter.ttk.Label(self,text="Result Matrix")
            self.CLabel.grid(row=len(matrixC)+2+1,column=0,pady=2,padx=10)
            self.resetList.append(self.CLabel)
            x=0
            self.labels=[]
            while x<len(matrixC):
                self.lab=tkinter.ttk.Label(self,text=f"{matrixC[x-1]} ")
                self.lab.grid(row=x+4+len(matrixC),column=0,pady=2,padx=10)
                self.labels.append(self.lab)
                self.resetList.append(self.lab)
                x+=1
        if self.operation.get()=="Subtract":
            matrixA=[]
            matrixB=[]
            for row in self.rowEntries:
                matrixA.append(list(map(int,(row.get()).split())))
            for row in self.columnEntries:
                matrixB.append(list(map(int,(row.get()).split())))
            matrixC=[]
            lst=[]
            for i in range(len(matrixA)):  
                lst=[]
                for j in range(len(matrixA[0])):
                    lst.append(matrixA[i][j] - matrixB[i][j])
                matrixC.append(lst)
                
            self.CLabel=tkinter.ttk.Label(self,text="Result Matrix")
            self.CLabel.grid(row=len(matrixC)+2+1,column=0,pady=2,padx=10)
            self.resetList.append(self.CLabel)
            x=0
            self.labels=[]
            while x<len(matrixC):
                self.lab=tkinter.ttk.Label(self,text=f"{matrixC[x-1]} ")
                self.lab.grid(row=x+4+len(matrixC),column=0,pady=2,padx=10)
                self.labels.append(self.lab)
                self.resetList.append(self.lab)
                x+=1
        if self.operation.get()=="Transpose":
            matrixA=[]
            matrixC=[]
            for row in self.rowEntries:
                matrixA.append(list(map(int,(row.get()).split())))
            for i in range(len(matrixA)):
                tmp=[]
                for j in range(len(matrixA[0])):
                    tmp.append(0)
                matrixC.append(tmp)
            for i in range(len(matrixA)):
                lst=[]
                for j in range(len(matrixA[0])):
                    matrixC[i][j]=matrixA[j][i]
            self.CLabel=tkinter.ttk.Label(self,text="Result Matrix")
            self.CLabel.grid(row=len(matrixC)+2+1,column=0,pady=2,padx=10)
            self.resetList.append(self.CLabel)
            x=0
            self.labels=[]
            while x<len(matrixC):
                self.lab=tkinter.ttk.Label(self,text=f"{matrixC[x]} ")
                self.lab.grid(row=x+4+len(matrixC),column=0,pady=2,padx=10)
                self.labels.append(self.lab)
                self.resetList.append(self.lab)
                x+=1
        
        if self.operation.get()=="Multiply":
            matrixA=[]
            matrixB=[]
            for row in self.rowEntries:
                matrixA.append(list(map(int,(row.get()).split())))
            for row in self.columnEntries:
                matrixB.append(list(map(int,(row.get()).split())))
            matrixC=[]
            for i in range(len(matrixA)):
                tmp=[]
                for j in range(len(matrixB[0])):
                    tmp.append(0)
                matrixC.append(tmp)
            lst=[]
            for i in range(len(matrixA)):
                for j in range(len(matrixB[0])):
                    for k in range(len(matrixB)):
                        matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
            self.CLabel=tkinter.ttk.Label(self,text="Result Matrix")
            self.CLabel.grid(row=len(matrixC)+2+1,column=0,pady=2,padx=10)
            self.resetList.append(self.CLabel)
            x=0
            self.labels=[]
            while x<len(matrixC):
                self.lab=tkinter.ttk.Label(self,text=f"{matrixC[x-1]} ")
                self.lab.grid(row=x+4+len(matrixC),column=0,pady=2,padx=10)
                self.labels.append(self.lab)
                self.resetList.append(self.lab)
                x+=1
        self.resetButton=tkinter.ttk.Button(self,text="Reset",command=self.resetAll)
        self.resetButton.grid(row=x+2+len(matrixC[0]),column=1,pady=2,padx=10)
    def resetAll(self):
        for i in self.resetList:
            if isinstance(i,list)==True:
                for j in i:
                    j.grid_remove()
            else: i.grid_remove()
        self.resetButton.grid_remove()
        self.rowLabel=tkinter.ttk.Label(self,text="Enter number of rows of Matrix A")
        self.rowLabel.grid(row=1,column=0,sticky="W",pady=5)
        self.rowEntry=tkinter.ttk.Entry(self,width=5)
        self.rowEntry.grid(row=1,column=1,sticky="W",pady=5)
        self.columnLabel=tkinter.ttk.Label(self,text="Enter number of columns of Matrix A")
        self.columnLabel.grid(row=2,column=0,sticky="W",pady=5)
        self.columnEntry=tkinter.ttk.Entry(self,width=5)
        self.columnEntry.grid(row=2,column=1,sticky="W",pady=5)
        self.rowBLabel=tkinter.ttk.Label(self,text="Enter number of rows of Matrix B")
        self.rowBLabel.grid(row=3,column=0,sticky="W",pady=5)
        self.rowBEntry=tkinter.ttk.Entry(self,width=5)
        self.rowBEntry.grid(row=3,column=1,sticky="W",pady=5)

        self.columnBLabel=tkinter.ttk.Label(self,text="Enter number of columns of Matrix B")
        self.columnBLabel.grid(row=4,column=0,sticky="W",pady=5)
        self.columnBEntry=tkinter.ttk.Entry(self,width=5)
        self.columnBEntry.grid(row=4,column=1,sticky="W",pady=5)
        self.mulLabel=tkinter.ttk.Label(self,text="In Case of multiplication\nrows of A Matrix Should be\nequal to Columns of B Matrix\nOtherwise\nDimensions of A Matrix Should be\nequal to Dimensions of B Matrix\nIn case of Transpose\nDont fill Matrix B dimensions")
        self.mulLabel.grid(row=5,column=0)    

window=MyWindow()
window.mainloop()
