# Method 1: RAISE EXCEPTION
ItemsInCart1 = 0
if ItemsInCart1 != 2:
    raise Exception("Products cart count not matching")

# Method 2: ASSERTION
ItemsInCart2 = 0
assert(ItemsInCart2 == 2)
