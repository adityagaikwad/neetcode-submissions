class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = "+-*/"

        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                if ch == "+":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(firstNum + secondNum)
                elif ch == "-":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(firstNum - secondNum)
                elif ch == "*":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(firstNum * secondNum)
                elif ch == "/":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(int(float(firstNum / secondNum)))
        
        return stack.pop()
