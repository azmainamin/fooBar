# Ion reflux relabelling

def answer(h, q):
    p = []
    # Step 1: Find row FROM BOTTOM UP of the elem in q in question
    for elem in q:
        x = elem
        for row in range(h,0,-1):
            vertices = (2**row) - 1
            if x % vertices == 0:
                break
            else:
                x = x % vertices
    # Step 2: If row == height, it is the root, since we are doing bottom up.  
        if row == h:
            p.append(-1)
    # Step 3: Find if right or left child
    
        #If right child. add 1
        elif x % 2 == 0:
            p.append(elem + 1)
        # If left child, add 2**i
        else:
            p.append(elem + (2**row))
    return p
	
