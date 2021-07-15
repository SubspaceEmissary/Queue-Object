# This is a WIP; expect errors by consequence.

class Queue():
    def __init__(self):
        self._requestlist = []
        self._admitlist = []
        
    def let(self):
        count = 0
        for item in self._requestlist:
            count += 1
            
        if count >= 1:
            self._requestlist.append(self._requestlist[-1] + 1)
        else:
            self._requestlist.append(1)
            
    def requisitions(self):
        return self._requestlist
    
    def admit(self):
            self._admitlist.append(self._requestlist[0])
            del self._requestlist[0]
    
    def admissions(self):
        return self._admitlist
