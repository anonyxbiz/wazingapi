from initialize import*

class Test:
    def __init__(self):
        self.view = 0
        self.visits = []
        self.unique = 0
        
    async def add(self):
        self.view +=1
        return 'ok'
    async def unique_visits(self, do):
        if do = "add":
            self.unique += 1
        return self.unique
        
    async def check(self, ip):
        if ip not in self.visits:
            self.visits.append(ip)
            await self.add()
            unique = await self.unique_visits('add')
            data = {"all_visits": self.view, "unique_visits": unique}            
        else:
            await self.add()
            unique = await self.unique_visits('nothing')
            data = {"all_visits": self.view, "unique_visits": unique}
        
        return data
        
if __name__ == '__main__':
    pass