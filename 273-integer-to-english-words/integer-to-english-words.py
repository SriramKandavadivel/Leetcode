class Solution:
    def numberToWords(self, num: int) -> str:
        to_19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to_19[n-1:n]
            if n < 100:
                return [tens[n//10 -2]] + words(n%10)
            if n < 1000:
                return [to_19[n//100 -1]] + ['Hundred'] + words(n%100)

            for i,w in enumerate(('Thousand', 'Million', 'Billion'),1): #statring from 1-idx,[1 indexed]
                if n < 1000**(i+1):
                    return words(n// 1000**(i)) + [w] + words(n% 1000**(i))
        
        return ' '.join(words(num)) or 'Zero'