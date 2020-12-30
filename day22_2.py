inpt = """Player 1:
42
29
12
40
47
26
11
39
41
13
8
50
44
33
5
27
10
25
17
1
28
22
6
32
35

Player 2:
19
34
38
21
43
14
23
46
16
3
36
31
37
45
30
15
49
48
24
9
2
18
4
7
20"""



def create_deck(inpt):
    p1=[]
    p2=[]
    
    flag = 0
    for i in inpt.split("\n"):
        if not flag:
            try:
                p1.append(int(i))
            except:
                pass
        else:
            try:
                p2.append(int(i))
            except:
                pass
            
        if i=="Player 2:":
            flag =1
    return p1,p2
def game(p1,p2,first=1):
    
    #print(f"======== GAME {first+1} ========= ")
    savep1=[]
    savep2=[]
    roun = 0
    while True:
        roun +=1
        #print(f"-- Round {roun} (Game {first+1})")
        #print("p1",p1)
        #print("p2",p2,"\n",)
        
        
        
        
       
        if p1 in savep1 or p2 in savep2:
            
            return ["p1"]+p1
            
        savep1.append(p1.copy())
        savep2.append(p2.copy())
        
        current1 = p1.pop(0)
        current2 = p2.pop(0)
        
        if current1<=len(p1) and current2<=len(p2):
            
            winner = game(p1.copy()[:current1],p2.copy()[:current2],first=first+1)
            
            if winner[0]=="p2":
                p2.extend([current2,current1])
            elif winner[0]=="p1":
                p1.extend([current1,current2])
            else:
                print(winner)
                input("wat")
                
            
        elif current1>current2:
            p1.extend([current1,current2])
        elif current1<current2:
            p2.extend([current2,current1])
        
        if p1==[] or p2==[]:
            if first==0:
                winner = (len(p1)>len(p2))*p1+(len(p1)<len(p2))*p2
                print(winner)
                cou=0
                for i in range(len(winner)):
                    
                    cou+=(i+1)*winner[-(i+1)]
                return cou
            else:
                winner = (len(p1)>len(p2))*(["p1"]+p1)+(len(p1)<len(p2))*(["p2"]+p2)
                return winner
def solve(inpt):
    p1,p2=create_deck(inpt)
    return game(p1,p2,first=0)
    

print(solve(inpt))