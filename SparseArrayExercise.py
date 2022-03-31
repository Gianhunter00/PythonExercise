
#to review, probably interpreted wrong
class SparseArray(object):
    def __init__(self, args):
        self.sparse_array = args
        
    def __len__(self):
        return len(self.sparse_array)
    
    def __getitem__(self, index):
        if index >= len(self):
            IndexError()
        return self.sparse_array[index]
    
    def __setitem__(self, index, value):
        if index >= len(self):
            IndexError()
        if value != 0:
            self.sparse_array[index] = value
            return
        
    def __delitem__(self, index):
        del self.sparse_array[index]
        
    def append(self, value):
        if value != 0:
            self.sparse_array.append(value)
            
            
sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
print(len(sa))
print(sa[0])
sa[2] = 5
print(sa[2])
del sa[0]
print(sa[0])
sa.append(6)
print(sa[-1])