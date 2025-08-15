import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        # l = paragraph.split()
        l= re.findall(r"[a-z]+(?:'[a-z]+)*", paragraph)
        # print(l)
        d = Counter(l)
        # print(d)
        for word in sorted(d, key=d.get, reverse= True):
            if word not in banned:
                return word
            print(word)