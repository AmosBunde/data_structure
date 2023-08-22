class Parenthesis:

    def IsPathensis(self, s:str) -> bool:
        stack = []
        closeToOpen = { ")":"(","]":"[","}":"{" }

        for t in s:
            if t in closeToOpen:
                if stack and stack [-1] == closeToOpen[t]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(t)
        return True if not stack else False
    

if __name__ == "__main__":
  
   new = Parenthesis()
   results = new.IsPathensis("(),{},[]")
   print(results)
