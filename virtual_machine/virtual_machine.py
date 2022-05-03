def calc(D, I): 
    
    W = []
    
    index = 0
    
    while index < len(I):
        
        i = I[index]
            
        if i == "load": 
            W.append(D[int(I[index+1])])
            index += 2
            continue
            
        if i == "print":
            print(W.pop())
            
        if i == "dup":
            temp = W.pop()
            W.append(temp)
            W.append(temp)
            
        if i == "add_two": 
            W.append(W.pop()+W.pop())
        
        if i == "mul_two": 
            W.append(W.pop()*W.pop())
            
        if i == "mod_two":
            b = W.pop()
            a = W.pop()
            W.append(a % b)
            
        if i == "input": 
            inp = input()
            W.append(inp)
            
        if i == "toint":
            temp = W.pop()
            W.append(int(temp))
            
        if i == "jump":
            index = int(I[index+1])
            continue
            
        if i == "jump_if":
            if len(W) > 0 and W[-1] == 0:
                index = int(I[index+1])
            else: 
                index = int(I[index+2])
            continue
                  
        index += 1
            