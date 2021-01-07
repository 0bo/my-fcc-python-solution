
def arithmetic_arranger(problems, solution=False):
  if len(problems) > 5:
    return "Error: Too many problems."
    
# must define line* first, can't be created automatically

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  
  for i, problem in enumerate(problems): # enumerate was not metioned in py4e
    num1, op, num2 = problem.split()

    if not op in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    if op == "+": # == is testing for equal, = is for assign
      # 'solution = int(num1) + int(num2)' throw error, as this 'solution' has conflict with the one in function parameters.
      result = int(num1) + int(num2)
    else:
      result = int(num1) - int(num2)

    space = max(len(num1),len(num2))

    line1 += num1.rjust(space+2)  # rjust is the key
    line2 += op + num2.rjust(space+1)
    line3 += "-" * (space+2)
    line4 += str(result).rjust(space+2)

    if i < len(problems)-1:
      line1 += "    "
      line2 += "    "
      line3 += "    "
      line4 += "    "

  arranged_problems = line1 + "\n" + line2 + "\n" + line3

  if solution == True:
    arranged_problems += "\n" + line4

  return arranged_problems
