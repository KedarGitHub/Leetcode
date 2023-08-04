class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output= list()
        max_val,counter=0,1
        if len(s)<=1:
            return len(s)
        else:
            for i in range(len(s)):
                output.append(s[i])
                for j in range(i, len(s)):
                    if j>i:
                        if s[j]!=s[i] and s[j] not in output:
                            output.append(s[j])
                            counter+=1
                        else:
                            if max_val < counter:
                                max_val = counter
                            counter=1
                            output.clear()
                            break          
            if max_val < counter:
                max_val = counter
            return max_val