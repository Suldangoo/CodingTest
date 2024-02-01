def solution(s, skip, index):
    answer = ''
    
    for i in s :
        loop = index
        
        while loop :
            if ord(i) >= 122 :
                i = 'a'
            else :
                i = chr(ord(i) + 1)
            
            if i not in skip :
                loop -= 1
                
        answer += i
    
    return answer