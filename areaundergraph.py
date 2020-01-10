equation = [3, 4, 5, 2]
def getY(equ, x) :
    value = 0
    for index, i in enumerate(equ) :
        value += i * (x**(len(equ)-index-1))
    return value    
def getArea(nod, startX, stopX) :
    areaSoFar = 0
    stepSize = (stopX-startX)/nod
    for i in range(nod * (stopX - startX)) :
        areaSoFar += getY(equation, (i/nod) + startX) * stepSize
    return areaSoFar

for i in range(10) :
    print("x:", i, "y:", getY(equation, i))

print(getArea(10, 0, 10))
print(getArea(100, 0, 10))
print(getArea(1000, 0, 10))
print(getArea(10000, 0, 10))