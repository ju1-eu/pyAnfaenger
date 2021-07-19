#import MyModule                # Alternative 1
#from MyModule import list_max  # Alternative 2
# from MyModule import *        # Alternative 3
import MyModule as mm           # Alternative 4


# Liste
l1 = [-2, 1, -10]

# Funktionsaufruf
#l1_max = MyModule.list_max(l1) # 1
#l1_max = list_max(l1)          # 2
l1_max = mm.list_max(l1)        # 4
l1_max
