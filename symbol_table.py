class Node:
    def __init__(self):
        self.identifier = ''
        self.scope = ''
        self.type = ''
        self.lineNo = 0
        self.next = None
    
    def __init__(self, key, value, Type, lineNo):
        self.identifier = key
        self.scope = value
        self.type = Type
        self.lineNo = lineNo
        self.next = None
    
    def print_node(self):
        print("Identifier's Name: ", self.identifier)
        print("Type: ", self.type)
        print("Scope: ", self.scope)
        print("Line Number: ", self.lineNo)

class SymbolTable:
    def __init__(self):
        self.head = [None] * 100
    
    def hashf(self, id):
        ascii_sum = sum(ord(c) for c in id)
        return ascii_sum % 100
    
    def insert(self, id, scope, Type, lineNo):
        index = self.hashf(id)
        p = Node(id, scope, Type, lineNo)
        
        if self.head[index] is None:
            self.head[index] = p
            print(f"{id} inserted")
            return True
        else:
            start = self.head[index]
            while start.next is not None:
                start = start.next
            start.next = p
            print(f"{id} inserted")
            return True
    
    def find(self, id):
        index = self.hashf(id)
        start = self.head[index]
        
        if start is None:
            return -1
        
        while start is not None:
            if start.identifier == id:
                start.print_node()
                return start.scope
            start = start.next
        
        return -1
    
    def delete_record(self, id):
        index = self.hashf(id)
        tmp = self.head[index]
        par = self.head[index]
        
        if tmp is None:
            return False
        
        if tmp.identifier == id and tmp.next is None:
            tmp.next = None
            del tmp
            return True
        
        while tmp.identifier != id and tmp.next is not None:
            par = tmp
            tmp = tmp.next
        
        if tmp.identifier == id and tmp.next is not None:
            par.next = tmp.next
            tmp.next = None
            del tmp
            return True
        
        elif tmp.identifier == id and tmp.next is None:
            par.next = None
            tmp.next = None
            del tmp
            return True
        
        return False
    
    def modify(self, id, scope, Type, lineNo):
        index = self.hashf(id)
        start = self.head[index]
        
        if start is None:
            return -1
        
        while start is not None:
            if start.identifier == id:
                start.scope = scope
                start.type = Type
                start.lineNo = lineNo
                return True
            start = start.next
        
        return False


if __name__ == '__main__':
    st = SymbolTable()
    print("**** SYMBOL_TABLE ****")
    
    # insert 'if'
    if st.insert("if", "local", "keyword", 4):
        print("if inserted")
    else:
        print("Failed to insert")
    
    # insert 'number'
    if st.insert("number", "global", "variable", 2):
        print("number inserted\n")
    else:
        print("Failed to insert")
    
    # find 'if'
    check = st.find("if")
    if check != -1:
        print("Identifier Is present")
    else:
        print("Identifier Not Present")
    
