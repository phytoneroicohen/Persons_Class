from Person import *

gay=Person("gay",14,"tel aviv",None)
gal=Person("gal",23,"yafo",None)
yoav=Person("yoav",60,"tel aviv",[gay,gal])
dana=Person("dana",0,"tel aviv",None)

yoav.add_child(dana)
yoav.print_children_names()




