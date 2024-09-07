from langchain.tools import tool

class CalculatorTool():
    @tool("make a calculation")
    def calculate(operation: str):
        """
        Useful to perform any mathematical calculation, like add, subtract, multiplication, division, etc.
        The input to this tool should be a mathematical expression, a couple examples are: '100*5' or 1000/2*5
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"