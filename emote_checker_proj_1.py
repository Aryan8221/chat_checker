# type your chat directory below
file = open("/Users/aryanneizehbaz/Downloads/chat checker.txt","r")
file2 = open("emotes.txt","r")
emotes=["lol","lmao","keepo","yep","pog"]
T = []
G=[]
for P, l in enumerate(file):
    if P in range(10000000):
        T.append(l[0:])
print(T[0])
q = input("enter the hour: ")
x = (input("enter starting min:"))
#y = (input("enter ending min:"))
minutes = input("enter minutes :")
# while True:
#     if int(T[y][15:16])==x:
#         y =+ 1
#         G.append(T[y-1])
#     elif T[y][15:16]== x+1:
#          y =+ 1
#          G.append(T[y - 1])
#     elif  T[y][15:16]== x+2:
#          y =+ 1
#          G.append(T[y - 1])
#     else:
#        break
'''while True  :
    if (T[0][15:16]==T[x][15:16]):
        x += 1
    elif (int(T[0][15:16]) == (int(T[x][15:16]))) +1:
        x += 1
    else:
        break
    if (int(T[0][15:16]) == (int(T[x][15:16]))) +2:
        x += 1'''
#while (int(T[0][15:16]) == (int(T[1085][15:16]))) - 1 :
#    x+=1
#print(x)
for z in T:
    for m in range(int(minutes)):
        if int(z[15:17]) == int(x)+(m):
            if int(q)==int(z[12:14]):
              G.append(z.strip())
        else:
            pass
# print(G)
for i in G:
    for b in emotes :
      if b in i:
          print(b +"....."+ i[0:25])
      else:
          pass
