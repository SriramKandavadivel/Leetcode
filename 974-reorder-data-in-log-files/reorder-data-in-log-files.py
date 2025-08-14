class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def func(x):
            s = x.split(" ")
            print(x)
            if x[-1].isdigit():
                return (1,)
            return (0," ".join(s[1:]), s[0])
        logs.sort(key = func)
        return logs