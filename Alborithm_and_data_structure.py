
# N = 191  K = 4 
def solution(N,K):

    res=[int(i) for i in str(N)]
    kb = K
    new = []

    for i in res:
        dum = i
        while(dum!=9):
            if kb == 0:
                break
            else:
                dum+=1
                kb-=1

        new.append(dum)
        listToStr = ''.join([str(j) for j in new])

    return listToStr
        
print(solution(512, 10))


# N = 191  K = 4 
def solution(N, K):

    i = 0

    while K>0 and i<3:
        N_str = str(N)
        tmp = int(N_str[i])
        if tmp ==9:
            i+=1

        else:
            new_str =N_str[:i]+str(tmp+1) + N_str[i+1:]
            if int(new_str) > N:
                N = int(new_str)
                K-=1

    return new_str

print(solution(981, 4))
































