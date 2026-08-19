class Solution:
    def compress(self, chars: List[str]) -> int:
        #read 
        i=0
        #write
        j=0

        while i < len(chars):
            #current character
            ch=chars[i]
            count=0

            while i < len(chars) and chars[i] == ch: #same char or not
                count+=1
                i+=1

            #write character with frequency
            chars[j] = ch
            j+=1

            if count>1:
                for digit in str(count):
                    chars[j] = digit
                    j+=1
        return j
