from __init__ import*

class Main:
    def __init__(self):
        self.view = 0
        
    async def add(self):
        self.view +=1
        return 'ok'
    
    async def check(self):
        await self.add()
        return self.view
        
if __name__ == '__main__':
    m = Main()
    data = a.run(m.check())
    p(data)