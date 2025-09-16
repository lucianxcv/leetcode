from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        # sorted(word) -> ['a','e','t']  --> ''.join -> "aet"
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())
