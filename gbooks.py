import math
class Book:
    def __init__(self,scr,Id):
        self.bookid=Id
        self.scan=False
        self.score=scr
class Library:
    def __init__(self,N,sign,M,Id):
        self.libraryid=Id
        self.numberOfBooks=N
        self.signup=sign
        self.max=M
        self.scanEstimate=math.ceil(self.max/self.numberOfBooks)
        self.booklist=[]
books=[]
libraries=[]

inputs=[]
file1 = open('c.txt', 'r') 
Lines = file1.readlines() 
count = 0
for line in Lines: 
    inputs=inputs+[line.strip()]
inputIndex=0

line1=inputs[inputIndex].split()
inputIndex+=1
totalBooks=int(line1[0])
totalLibraries=int(line1[1])
totalDays=int(line1[2])

newline=inputs[inputIndex].split()
inputIndex+=1

ind=0
for i in range(totalBooks):
    newB=Book(int(i),ind)
    books=books+[newB]
    ind+=1
ind=0
for i in range(totalLibraries):
    newline=inputs[inputIndex].split()
    inputIndex+=1
    newLib=Library( int(newline[0]), int(newline[1]), int(newline[2]), ind )
    ind+=1
    libBooks=inputs[inputIndex].split()
    inputIndex+=1
    j=0
    for k in libBooks:
        libBooks[j]=books[int(libBooks[j])]
        j+=1
    newLib.booklist=newLib.booklist+libBooks
    libraries=libraries+[newLib]

def bubbleSortLibrary(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].signup > arr[j+1].signup :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def bubbleSortBook(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].score > arr[j+1].score :
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSortLibrary(libraries)
t=0
libsigned=0
output=[[0]]

for i in libraries:
    if (i.signup+(i.scanEstimate/2)<=totalDays and t<totalDays):
        selectedBooks=[]
        
        itsBookList=i.booklist
        t=t+i.signup
        bubbleSortBook(itsBookList)
        for k in itsBookList:
            if (books[k.bookid].scan==False and math.ceil(len(selectedBooks)/i.max)<=(totalDays-t)):
                selectedBooks=selectedBooks+[k.bookid]
                books[k.bookid].scan=True
        if(len(selectedBooks)>0):   
            libsigned+=1     
            arr1=[i.libraryid, len(selectedBooks)]
            output=output+[arr1]
            arr1=[]
            for g in selectedBooks:
                arr1=arr1+[g]
            output=output+[arr1]
            
output[0][0]=libsigned
for i in output:
    for j in i:
        print(j, end=" ")
    print()
