class Solution:
    def handleCount(self, count, chars, start):
        count_list = []
        while count >= 1:
            count_list.append(count % 10)
            count = count // 10

        count_list.reverse()
        for x in range(len(count_list)):
            start += 1
            chars[start] = str(count_list[x])

        return start, chars

    def compress(self, chars: List[str]) -> int:
        start, end = 0, 0
        while end < len(chars):
            curr = chars[start]
            while end < len(chars) and chars[start] == chars[end]:
                # print(chars[start], chars[end])
                # print(start, end)
                end += 1
            count = end - start
            if count > 1:
                start, chars = self.handleCount(count, chars, start)
            start += 1
            while start < len(chars) and chars[start] == curr:
                del chars[start]

            end = start

        
        return len(chars)
        