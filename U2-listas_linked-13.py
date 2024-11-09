#13
class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.next= None

class list:
    def __init__(self):
        self.head= None

    def end(self, valor):
        newnodo = Nodo(valor)

        if self.head is None:
            self.head= newnodo
        else:
            last= self.head
            while last.next:
                last = last.next
            last.next = newnodo
    def printlist(self):
        last = self.head
        while last:
            print(last.valor, end=" -> ")
            last = last.next
        print("None")

if __name__ == "__main__":
    list= list()

list.end(4)
list.end(4)
list.end(6)
list.end(3)
list.printlist()