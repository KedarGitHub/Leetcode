class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = list()
        counter,max_value,flag=0,0,0;

#     if s.isspace():   # checks if python string has space or not 
#         return len(s)
#     else:

        if len(s)==1:
            return len(s)
        else:
            for i in s:
    #             print('Hey1')
                if i not in output:
    #                 print('Hey2')
                    if i.isspace() and flag==0:
                        flag=1
                        counter+=1
                    elif i.isspace() and flag==1:             
                        output.clear()
                        if max_value < counter:
    #                         print('Hey4')
                            max_value=counter
                        counter=1
                    else:
                        output.append(i)
                        counter+=1
                elif i in output:
    #                 print('Hey3')
                    output.clear()
                    output.append(i)
                    if max_value < counter:
    #                     print('Hey4')
                        max_value=counter
                    counter=1
            if max_value < counter:
    #                   print('Hey4')
                        max_value=counter 
            return max_value
