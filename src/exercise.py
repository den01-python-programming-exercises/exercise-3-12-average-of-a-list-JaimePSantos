def main():
    #write your code below this line
    intList = []
    cardinality=0
    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)
    sum = 0
    for i in range(len(intList)):
      sum+=intList[i]
      cardinality+=1
    print("Average: %s"%(sum/cardinality))

if __name__ == '__main__':
    main()
