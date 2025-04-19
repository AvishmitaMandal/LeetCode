class Solution:
    def parseLog(self, log):
        i = 0
        while log[i] != ':':
            i += 1
        idx = log[:i]
        i += 1
        k = i
        while log[k] != ':':
            k += 1
        status = log[i:k]
        time = log[k+1:]
        return int(idx), status, int(time)

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []

        parsed_logs = []
        for x in range(len(logs)):
            log = logs[x]
            idx, status, time = self.parseLog(log)
            parsed_logs.append([idx, status, time])

        sorted_parsed_logs = sorted(parsed_logs, key = lambda x : x[2])
        print(sorted_parsed_logs)

        for x in range(len(sorted_parsed_logs)):
            log = sorted_parsed_logs[x]
            if len(stack) == 0:
                stack.append(log)
                continue
            prev_log = sorted_parsed_logs[x-1]
            if log[1] == "end":
                if prev_log[1] == "start":
                    res[log[0]] += (log[2]-prev_log[2]+1)
                else:
                    res[log[0]] += (log[2]-prev_log[2])
                stack.pop()
            else:
                if prev_log[1] == "end":
                    diff = (log[2]-prev_log[2]-1)
                else:
                    diff = (log[2]-prev_log[2])
                temp = stack.pop()
                res[temp[0]] += diff
                stack.append(temp)
                stack.append(log)

        

        return res


        

            

        