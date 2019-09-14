from random import choice
npart=500
side=35
time=10
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
for ipart in range(npart):
    x,y = side//2,side//2
    counter=0
    while 1:
        counter+=1
        grid[x][y]=0
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
            time+=counter
            break
        grid[x][y]=1
avetime=time/npart
print("<t>=%5.2f <t>/r2=%5.2f"%(avetime, avetime/(side**2)))
