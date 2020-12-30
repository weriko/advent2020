import numpy as np
inpt = """.###.#.#
####.#.#
#.....#.
####....
#...##.#
########
..#####.
######.#"""



def count(inpt,i,j,k,w): #wow st this is inefficient, this will take a long ass time 
    try:
       
        l = [inpt[i+1][j-1][k+1][w],
             inpt[i+1][j][k+1][w],
             inpt[i+1][j+1][k+1][w],
             inpt[i][j-1][k+1][w],
             inpt[i][j][k+1][w],
             inpt[i][j+1][k+1][w],
             inpt[i-1][j-1][k+1][w],
             inpt[i-1][j][k+1][w],
             inpt[i-1][j+1][k+1][w],
             
             inpt[i+1][j-1][k][w],
             inpt[i+1][j][k][w],
             inpt[i+1][j+1][k][w],
             inpt[i][j-1][k][w],
             
             inpt[i][j+1][k][w],
             inpt[i-1][j-1][k][w],
             inpt[i-1][j][k][w],
             inpt[i-1][j+1][k][w],
             
             inpt[i+1][j-1][k-1][w],
             inpt[i+1][j][k-1][w],
             inpt[i+1][j+1][k-1][w],
             inpt[i][j-1][k-1][w],
             inpt[i][j][k-1][w],
             inpt[i][j+1][k-1][w],
             inpt[i-1][j-1][k-1][w],
             inpt[i-1][j][k-1][w],
             inpt[i-1][j+1][k-1][w],
             
             
             
             inpt[i+1][j-1][k+1][w+1],
             inpt[i+1][j][k+1][w+1],
             inpt[i+1][j+1][k+1][w+1],
             inpt[i][j-1][k+1][w+1],
             inpt[i][j][k+1][w+1],
             inpt[i][j+1][k+1][w+1],
             inpt[i-1][j-1][k+1][w+1],
             inpt[i-1][j][k+1][w+1],
             inpt[i-1][j+1][k+1][w+1],
             
             inpt[i+1][j-1][k][w+1],
             inpt[i+1][j][k][w+1],
             inpt[i+1][j+1][k][w+1],
             inpt[i][j-1][k][w+1],
             inpt[i][j][k][w+1],
             inpt[i][j+1][k][w+1],
             inpt[i-1][j-1][k][w+1],
             inpt[i-1][j][k][w+1],
             inpt[i-1][j+1][k][w+1],
             
             inpt[i+1][j-1][k-1][w+1],
             inpt[i+1][j][k-1][w+1],
             inpt[i+1][j+1][k-1][w+1],
             inpt[i][j-1][k-1][w+1],
             inpt[i][j][k-1][w+1],
             inpt[i][j+1][k-1][w+1],
             inpt[i-1][j-1][k-1][w+1],
             inpt[i-1][j][k-1][w+1],
             inpt[i-1][j+1][k-1][w+1],
             
             
             
             
             inpt[i+1][j-1][k+1][w-1],
             inpt[i+1][j][k+1][w-1],
             inpt[i+1][j+1][k+1][w-1],
             inpt[i][j-1][k+1][w-1],
             inpt[i][j][k+1][w-1],
             inpt[i][j+1][k+1][w-1],
             inpt[i-1][j-1][k+1][w-1],
             inpt[i-1][j][k+1][w-1],
             inpt[i-1][j+1][k+1][w-1],
             
             inpt[i+1][j-1][k][w-1],
             inpt[i+1][j][k][w-1],
             inpt[i+1][j+1][k][w-1],
             inpt[i][j-1][k][w-1],
             inpt[i][j][k][w-1],
             inpt[i][j+1][k][w-1],
             inpt[i-1][j-1][k][w-1],
             inpt[i-1][j][k][w-1],
             inpt[i-1][j+1][k][w-1],
             
             inpt[i+1][j-1][k-1][w-1],
             inpt[i+1][j][k-1][w-1],
             inpt[i+1][j+1][k-1][w-1],
             inpt[i][j-1][k-1][w-1],
             inpt[i][j][k-1][w-1],
             inpt[i][j+1][k-1][w-1],
             inpt[i-1][j-1][k-1][w-1],
             inpt[i-1][j][k-1][w-1],
             inpt[i-1][j+1][k-1][w-1],

             ]
       
       
        
        
        
        
        return l.count(1)
    except Exception as e:
        
        #return count(expand(inpt),i,j,k)
        #print(e)
        pass


def helper(inpt):
    temp = inpt.copy()
    for i in range(len(inpt)):
        for j in range(len(inpt)):
            for k in range(len(inpt)):
                for w in range(len(inpt)):
                    ctd = count(inpt,i,j,k,w)
                    if inpt[i][j][k][w]==1:
                        if not (ctd==2 or ctd==3):
                            temp[i][j][k][w]=0
                    if inpt[i][j][k][w]==0:
                        if ctd==3:
                            temp[i][j][k][w]=1
    return temp
  
def expand(inpt):
    
    inpt = np.pad(inpt,[(1,),(1,),(1,),(1,)],mode="constant")
    return inpt  
    
def solve(inpt):
    inpt = inpt.replace(".","0")
    inpt = inpt.replace("#","1")
    
    inpt = inpt.split("\n")
    temp = []
    for i in range(len(inpt)):
        temp.append([])
        for j in range(len(inpt)):
            temp[i].append(int(inpt[i][j]))
            
    inpt = np.array(temp)
    inpt =np.expand_dims(inpt, 0) #Just bruteforce it :)
    inpt =np.expand_dims(inpt, 0)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    inpt = expand(inpt)
    
    for i in range(6):
        print(inpt)
        print(i)
        inpt = expand(inpt)
        inpt = helper(inpt)
        
        
    
    print(inpt)
    print(np.count_nonzero(inpt))
   
print(solve(inpt))
    
    

                    