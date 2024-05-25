# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self,words):
       if not words:
           return []
       match_word=[word for word in words if sorted(self.word)==sorted(word)]
       
       if not match_word:  
            return []
        
       return match_word
    
listen = Anagram("listen")


