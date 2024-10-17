def is_anagram(s:str, t:str):
    if len(s) != len(t):
        return False
    
    palavra1 = ''.join(sorted(s.upper()))
    palavra2 = ''.join(sorted(t.upper()))
    
    return palavra1 == palavra2

def is_anagram_professor(s, t):
    return sorted(s) == sorted(t)

print(is_anagram_professor('amor', 'roma'))