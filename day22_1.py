inpt = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

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


def solve(inpt):
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
    while True:
        current1 = p1.pop(0)
        current2 = p2.pop(0)
        if current1>current2:
            p1.extend([current1,current2])
        else:
            p2.extend([current2,current1])
        if p1==[] or p2==[]:
            winner = (len(p1)>len(p2))*p1+(len(p1)<len(p2))*p2
            cou=0
            for i in range(len(winner)):
                
                cou+=(i+1)*winner[-(i+1)]
            return cou
    print(p1,p2)
print(solve(inpt))