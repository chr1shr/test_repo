for i in range(1,21):
    s=1
    for j in range(1,i+1):
        s*=j
    print("%d!=%d" %(i,s))
