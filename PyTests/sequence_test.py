class MySeq:
    def __init__(self):
        self.l = list(range(10))
    
    def __getitem__(self, index):
        return self.l.__getitem__(index)

seq = MySeq()
for i in seq:
    print(i,end='-')    # 0-1-2-3-4-5-6-7-8-9-

print()

*sseq,_ = seq
print(sseq)             # [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(seq[:-1])         # [0, 1, 2, 3, 4, 5, 6, 7, 8]