class Solution:
    def calPoints(self, ops):
        record = []
        for i in range(len(ops)):
            try:
                record.append(int(ops[i]))
            except:
                pass
            if ops[i] == "+":
                record.append(sum(record[-2:]))
            elif ops[i] == "D":
                record.append(2 * record[-1])
            elif ops[i] == "C":
                record.pop()
        return sum(record)