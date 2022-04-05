
#to review, probably interpreted wrong
class SparseArray(object):
    def __init__(self, args):
        self.length = len(args)
        self.dict = {key: value for key,value in enumerate(args) if value != 0}
            
        
    def __len__(self):
        return self.length
    
    def __getitem__(self, index):
        if index >= len(self):
            IndexError()
        if index < 0:
            index += self.length + 1
        return self.dict[index] if index in self.dict else 0
    
    def __setitem__(self, index, value):
        if index >= len(self):
            IndexError()
        if value != 0:
            self.dict[index] = value
        
    def __delitem__(self, index):
        if index in self.dict:
            del self.dict[index]
        
    def append(self, value):
        if value != 0:
            self.length += 1
            self.dict[self.length] = value
    
sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
print(len(sa))
print(sa[0])
sa[2] = 5
print(sa[2])
del sa[0]
print(sa[0])
sa.append(6)
print(sa[-1])