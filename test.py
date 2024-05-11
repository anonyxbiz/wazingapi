from initialize import*

class Test:
    def __init__(self):
        self.view = 0
        self.visits = []
        
    async def add(self):
        self.view +=1
        return 'ok'
    
    async def check(self, ip):
        if ip not in self.visits:
            self.visits.append(ip)
            await self.add()
            
        return self.view
        
if __name__ == '__main__':
    pass