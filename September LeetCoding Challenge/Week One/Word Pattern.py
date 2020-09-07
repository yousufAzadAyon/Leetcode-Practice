class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        words = str.split()
        
        if len(pattern) != len(words):
            return False
        
        character_word = dict()
        used_words = set()
        
        for character, word in zip(pattern, words):
            if character not in character_word and word not in used_words:
                character_word[character] = word
                used_words.add(word)
            elif character not in character_word and word in used_words:
                return False
            elif character_word[character] != word:
                return False
            
        return True