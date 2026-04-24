from collections import Defaultdict 

# Pour ce type de problème 
# Il faut donc trouver une "signature" (une clé) identique pour tous les anagrammes,
# puis regrouper les mots qui partagent la même signature dans un dictionnaire (hash map).

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = Defaultdict(list)
        for word in strs : 
            # Sorted retourne toujours une liste pas une chaine 
            key = ''.join(sorted(word))
            groups[key].append(word)
            
        return list(groups.values())
    
    
# 2eme solution sans Defaultdict (leetcode friendly)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for word in strs : 
            key = ''.join(sorted(word))
            if key in groups: 
                groups[key].append(word)
            else : 
                groups[key] = [word]
        return list(groups.values())
        
        
        