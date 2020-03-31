from math import sqrt
MAX=999999999
def costMin(matrix,start, end=None):
        actualNode = start
        visited = [actualNode]
        cost = 0
        while end not in visited and len(visited) < len(matrix):
            lst = [el for el in matrix[actualNode]]
            while lst.index(min(lst)) in visited:
                lst[lst.index(min(lst))] = MAX
            for x in lst:
                if(x==0):
                    lst[lst.index(x)]= MAX
            cost += min(lst)
            actualNode = lst.index(min(lst))
            visited.append(lst.index(min(lst)))
        if end is None:
            cost += matrix[visited[-1]][start]
        return (cost,visited)

def readMatrix(fileName,k=0):
        f=open(fileName)
        lines=f.readlines()
        list=[]
        if(k==0):
            k=len(lines)-1
        for i in range(7,k):
            currentLine=lines[i].split(" ")
            list.append((float(currentLine[0]),float(currentLine[1])))
        mat=[]
        for i in range(0,k-7):
            print(str(i)+" out of "+str(k))
            x1,y1=list[i]
            currentNode=[]
            for j in range(0,k-7):
                
                x2,y2=list[j]
                currentNode.append(sqrt((x1-x2)**2+(y1-y2)**2))
            mat.append(currentNode)

        net={}
        net['mat']=mat
        net['noNodes']=len(mat)
        return net

        
    


def readFromFile(fileName):
        f=open(fileName)
        net={}
        matrix=[]
        a=int(f.readline())
        for x in range(a):
            x=f.readline()
            z=x.split(",")
            list=[]
            for s in z:
                list.append(int(s))
            matrix.append(list)
        net["noNodes"]=a
        net["mat"]=matrix
        return net

def test1(fileName):
    f=open(fileName)
    net={}
    matrix=[]
    a=f.readlines()
    for x in a:
           z=x.split("      ")
           list=[]
           for s in z:
               list.append(int(s))
           matrix.append(list)
    net['noNodes']=len(matrix)
    net['mat']=matrix
    return net


def lenPath(list,problParams):
    sum=0
    for i in range(0,len(list)-1):
        sum+=problParams['mat'][list[i]][list[i+1]]
    return sum