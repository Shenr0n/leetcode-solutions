class Solution:
    def calPoints(self, operations: List[str]) -> int:
        opStack = []

        for op in operations:
            if op == "+":
                opStack.append(opStack[-1]+opStack[-2])
            elif op == "D":
                opStack.append(2*opStack[-1])
            elif op == "C":
                opStack.pop()
            else:
                opStack.append(int(op))

        return sum(opStack)
        
