class Solution:
    def compress(self, chars: List[str]) -> int:
        start, end = 0, 0
        while end < len(chars):
            curr = chars[start]
            while end < len(chars) and chars[start] == chars[end]:
                # print(chars[start], chars[end])
                # print(start, end)
                end += 1
            count = end - start
            if count >= 1000:
                chars[start+1] = str(count//1000)
                count = count % 1000
                chars[start+2] = str(count//100)
                count = count % 100
                chars[start+3] = str(count//10)
                count = count % 10
                chars[start+4] = str(count)
                start = start + 4
            elif count >= 100:
                chars[start+1] = str(count//100)
                count = count % 100
                chars[start+2] = str(count//10)
                count = count % 10
                chars[start+3] = str(count)
                start = start + 3
            elif count >= 10:
                chars[start+1] = str(count//10)
                count = count % 10
                chars[start+2] = str(count)
                start = start + 2
            elif count > 1:
                chars[start+1] = str(count)
                start = start + 1
            start += 1
            while start < len(chars) and chars[start] == curr:
                del chars[start]

            end = start

        
        return len(chars)
        