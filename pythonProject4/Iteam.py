class Item:
    #CBCBE00775590000001119 /100796689282
    def CalculatePrice(self,x,y):
        return x*y

item = Item()
item.Name='Honey'
item.Price=1000
item.quanty=5
print(item.CalculatePrice(item.Price,item.quanty))

item2 =Item()
item2.Name="N.Sugar"
item2.Price=75
item2.quanty=5
print(item2.CalculatePrice(item2.Price,item2.quanfty))