from rectangle import rectangle
from surface import surface

r = rectangle(10, 10, 10, 10)
assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
r = rectangle(-1, 1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (-1,1,1,1))
r = rectangle(1, -1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,-1,1,1))
r = rectangle(1, 1, -1, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,-1,1))
r = rectangle(1, 1, 1, -1)
assert((r.x, r.y, r.height, r.width) == (1,1,1,-1))

s = surface("myimage.png", 10, 10, 10, 10)
assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
s.rect = s.getRect()
assert(s.rect.x, s.getRect().y, s.rect.height, s.rect.width) == (10,10,10,10)
assert s.image 
print("Test Complete!")

