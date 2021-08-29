class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs = []
        lets = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digs.append(log)
            else:
                lets.append(log)
                
        lets.sort(key = lambda x: x.split()[0])
        lets.sort(key = lambda x: x.split()[1:])
        res = lets + digs
        return res