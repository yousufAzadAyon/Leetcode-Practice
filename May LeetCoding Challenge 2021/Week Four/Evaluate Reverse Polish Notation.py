class Solution:
	def evalRPN(self, tokens) -> int:
		stack = []

		for token in tokens:
			if token.isnumeric():
					number = int(token)
					stack.append(number)
			else:
				if token == "+":
					res = stack.pop() + stack.pop()
					stack.append(res)
				elif token[0] == "-":
					if len(token) > 1:
						number = -int(token[1:])
						stack.append(number)
					else:
						second = stack.pop()
						first = stack.pop()
						res = first - second
						stack.append(res)
				elif token == "*":
					res = stack.pop() * stack.pop()
					stack.append(res)
				else:
					divisor = stack.pop()
					dividend = stack.pop()
					res = int(dividend / divisor)            
					stack.append(res)
		return stack[0]