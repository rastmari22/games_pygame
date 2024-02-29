from Block import Block
class Wall():
    def __init__(self,arr_bl):
        self.arr_bl=arr_bl

    def exist(self):#y
        # for line in self.arr_bl:
        for block in self.arr_bl:
            if block.visible:
                return True
        return False

    def show(self):#y
        for block in self.arr_bl:
            if block.visible:
                block.show()