def lenght(object): # Sama seperti fungsi len()
    count = 0
    for i in object:
        count += 1
    return count

def CSVParser(raw): # Untuk read file CSV dan memindahkan ke array 2D
    matrix = []
    for i in range(lenght(raw)):
        tempList = []
        tempString = ""
        for j in range(lenght(raw[i])):
            if(raw[i][j] == ';' or raw[i][j] == '\n'):
                tempList += [tempString]
                tempString = ""
            else:
                tempString += raw[i][j]
        matrix += [tempList]
    return matrix

def sorting(arr, idx): # Melakukan sorting ascending suatu arr berdasarkan parameter idx
    tempArr = arr
    for i in range(lenght(arr)-1):
        for j in range(lenght(arr)-1, i, -1):
            if(tempArr[j][idx] < tempArr[j-1][idx]):
                temp = tempArr[j][idx]
                tempArr[j][idx] = tempArr[j-1][idx]
                tempArr[j-1][idx] = temp
    return tempArr