class StringUtility:
    
    def __init__(self, string):
        self.s = string
        
    def __str__(self):
        return self.s

    def vowels(self):
        count = 0
        for a in self.s:
            if a in 'aeiouAEIOU':
                count += 1 
        if count < 5:
            return (f"{count}")
        elif count >=5:
            return ("many")

    def bothEnds(self):
        if len(self.s) <= 2:
            return ''
        else:
            return (f"{self.s[0]}{self.s[1]}{self.s[-2]}{self.s[-1]}")

    def fixStart(self):
        star = "*"
        if len(self.s) > 1:
            res = self.s[0] + self.s[1:].replace(self.s[0], star)
            return res
        else:
            return self.s

    def asciiSum(self):
        SUM = 0
        for char in self.s:
            value = ord(char)
            SUM += value
        return SUM

    def cipher(self):
        cip = ''
        for char in self.s:
            if char ==' ':
                cip = cip+char
            elif char.isupper():
                cip = cip+chr((ord(char)+len(self.s)-65)%26+65)
            else:
                cip = cip+chr((ord(char)+len(self.s)-97)%26+97)
        return cip

        
        






            
       
        
 
   




   
        
 
        
       

        
            
