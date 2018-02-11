
def bubblesort(DataList):
    for i in range(len(DataList)-1):
        for j in range(len(DataList)-1-i):
            if DataList[j] > DataList[j+1]:
                DataList[j], DataList[j+1] = DataList[j+1], DataList[j]
    return DataList

DataList = [3,5,6,1,4]
bubblesort(DataList)
print DataList