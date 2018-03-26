#title           : blockchain.py
#description     : blockchain basics
#author          : Tochi Opara
#date            : 3-26-2018
#python_version  : 3  
#==============================================================================

import datetime
import time
import pickle
import os

class PersistentDataHandler:
    def __init__(self):
        self.__knowledge = list()

    """
     This method loads the data from the file and retuns a list.
     precondition:
           The Persistent instance exist and the file exist in the folder
     postcondition: A list is return to by the methods.
     
    """
    def loaddata(self,file):
        try:
            with open(file,"rb") as knowfile:
                None
        except:
            self.dumpdata(self.__knowledge,file)
        finally:
            if os.path.getsize(file) > 0:
                with open(file,"rb") as knowfile:
                    self.__knowledge = pickle.load(knowfile)
        return self.__knowledge

    """
       Name: dumpdata
       dumps the data to the to tehe file..
       precondition:
       postcondition:
       paramaters:
       
    """
    def dumpdata(self,knowledge,file):
        with open(file,"wb") as knowfile:
            pickle.dump(knowledge,knowfile)
        return
    
class Block:
    MaxValue = 128
    BlockCount = 0
    
    def __init__(self,value):
        Block.BlockCount = Block.BlockCount + 1
        self.__value = value
        self.PNodeKey = 0
        self.CPublicKey = self.hashFunction()
        self.__BC = Block.BlockCount
        self.__time =""
        
    def hashFunction(self):
        res = [ord(i) for i in self.__value]
        asc = sum(res)
        key = ((Block.MaxValue**2)+1)/(Block.BlockCount+asc)
        return key
    
    def getBlockCount(self):
        return self.__BC

    def getValue(self):
        return self.__value

    def setPNodeKey(self,prev):
        if Block.BlockCount == 1:
            self.PNodeKey = 0
        else:
            self.PNodeKey = prev

    def getPNodeKey(self):
        return self.PNodeKey

    def setTime(self,time):
        self.__time = time

    def getTime(self):
        return self.__time


class Transaction(Block):
    MaxTransaction = 128
    BlockCount = 0

    def __init__(self,tran=None,col=None):
        self.__Transaction = tran
        self.__colision = col

    def setTransactionList(self,tran):
        self.__Transaction = tran
        
    def setCollision(self,col):
        self.__colision = col

    def collision(self,hv):
        if hv in self.__colision:
            while True:
                hv = hv + 1
                if hv not in self.__colision:
                    self._colision.append(hv)
                    return hv
        else:
            hashValue.append(hv)
            return hv

    def addBlock(self,value):
        if len(self.__Transaction) <= Transaction.MaxTransaction:
            print("Enter now")
            block = Block(value)
            block.setTime(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            if (block.CPublicKey not in  self.__colision):
                if (len(self.__Transaction) ==1):
                    self.__colision.append(block.CPublicKey)
                    self.__Transaction.append(block)
                elif (len(self.__Transaction) > 1):
                    self.__colision.append(block.CPublicKey)
                    temp = self.__Transaction[len(self.__Transaction)-1 ]
                    block.setPNodeKey(temp.CPublicKey)
                    self.__Transaction.append(block)
                    
            else:
                
                newKey = self.collision(block.CPublicKey)
                block.CPublicKey(newKey)
                temp = self.__Transaction[len(self.__Transaction)-1]
                block.setPNodeKey(temp.CPublicKey)
                self.__Transaction.append(block)
                self.__colision.append(block.CPublicKey)
        else:
            print("The Transaction size is: ",Transaction.MaxTransaction,", no more block can be added to the Transaction")

    def TransactionCount(self):
        return len(self.__Transaction)

    def MaxTransactionCount(self):
        return Transaction.MaxTransaction

    def collision(self):
        return self.__colision
    
    def transaction(self):
        return self.__Transaction

    def printBlock(self):
        output=""
        output += "_"*153 + "\n|"
        for i,k in enumerate(self.__Transaction):
            
            output +='block Number: {} | Value: {} | Previous Block key value: {} | Current Node Key Value: {} | TimeStamp: {}'.format(i+1,k.getValue(),k.getPNodeKey(),k.CPublicKey,k.getTime())
            output += "\n"+"_"*153
            output +="\n"
        print(output)

    def printTransactionValue(self):
        output =""
        for i,k in enumerate(self.__Transaction):
            output += '[{} | {}]   '.format(i+1,k.getValue())
        return output



def menu():
    output="1)\tAddBlock\n2)\tDisplay Transaction Count\n3)\tPrint Block\n4)\tPrint Transaction Value(s)\n5)\tPrint Maximum number of Block\n6)\tTerminate"
    print(output)
    

def number():
    #number
    num = input("Enter a number from the menu: ")
    while not(num.isdigit()):
        print("Number entered is not a digit! please enter a digit.")
        num = input("Enter a number from the menu: ")
    while int(num) <=0 or int(num) >6 or not(num.isdigit()):
        print("Choice do not exist. Choose from 1 to 6")
        num = input("Enter a number from the menu: ")
        while not(num.isdigit()):
            print("Number entered is not a digit! please enter a digit.")
            num = input("Enter a number from the menu: ")
    return int(num)

        
def main():
    print("\tTransaction Block Menu\n")
    menu()
    print("\n")
    val = number()
    data = PersistentDataHandler()
    tr = data.loaddata("transaction.txt")
    cs = data.loaddata("collision.txt")
    
    trans = Transaction(tr,cs)
    
    while (val != 6):
        if val == 1:
            print()
            val = input("Enter the block value: ")
            trans.addBlock(val)
            data.dumpdata(tr,"transaction.txt")
            data.dumpdata(cs,"collision.txt")
            print()
        elif val == 2:
            print("The Transaction Count is: ",trans.TransactionCount())
            print()
        elif val == 3:
            trans.printBlock()
            print()
        elif val == 4:
            print("The Transaction Value(s)",trans.printTransactionValue())
            print()
        elif val == 5:
            print("The Maximum Transaction is: ",trans.MaxTransactionCount())
            print()
            
        print()
        menu()
        print()
        val = number()
        print()
    

if __name__=="__main__":
    main()
