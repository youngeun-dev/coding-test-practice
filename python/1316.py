num = int(input()) # 반복할 숫자 입력                                        
group_word=0 # 그룹 숫자 개수                                               
                                                                      
for _ in range(num):                                                  
    word=input()                                                      
    error=0                                                           
    for index in range(len(word)-1):                                  
# len(word)로 실행했더니 index가 range 범위를 벗어났다는 에러가 떴다                      
        if word[index] != word[index+1]:                              
            new_word = word[index+1]                                  
            if new_word.count(word[index]) > 0:                       
                error+=1                                              
    if error == 0:                                                    
        group_word+=1                                                 
                                                                      
print(group_word)                                                     
                                                                      
