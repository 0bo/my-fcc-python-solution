class Category:
  def __init__(self, category):
    self.name = category
    self.ledger = []
  
  def deposit(self, amount, description = None):
    if description == None:
      self.ledger.append({"amount": amount, "description": ''})
    else:
       self.ledger.append({"amount": amount, "description": description})
  
  def get_balance(self):
    current_balance = 0
    for item in self.ledger:
      current_balance += item["amount"]
    return current_balance

  def check_funds(self, amount):
    return amount <= self.get_balance() 
    #current_balance = self.get_balance
    #if current_balance - amount < 0:
    #  return False
    #else:
    #  return True

  def withdraw(self, amount, description = None):
    if self.check_funds(amount) == False:
      return False
    else:  
      if description == None:
        self.ledger.append({"amount": -(amount), "description": ''})
      else:
        self.ledger.append({"amount": -(amount), "description": description})
      return True

  def transfer(self, amount, new_category):
    if self.check_funds(amount) == False:
      return False
    else:
      self.ledger.append({'amount' : -(amount), 'description': f"Transfer to {new_category.name}"})
      new_category.deposit(amount, "Transfer from %s"%(self.name))
      return True

  def __str__(self):
    output = self.name.center(30,"*")
    for item in self.ledger:
      try:
        item_desc = item["description"][0:23]
      except:
        item_desc = ''
      item_amnt = str('{:.2f}'.format(item['amount']))
      output += f"\n{item_desc:<23}{item_amnt:>7}"
    total_amount = str(self.get_balance())
    output += f"\nTotal: {total_amount}"
    return  output


def create_spend_chart(categories):
  cates_spend = {}
  for cate in categories:
    cate_sum = 0
    for item in cate.ledger:
      if item["amount"] < 0:
        cate_sum += abs(item["amount"])
      cates_spend[cate.name] = round(cate_sum,2)
  total_spend = sum(cates_spend.values())
  cates_percent ={}
  for cate in cates_spend.keys():
    cates_percent[cate] = int(round(cates_spend[cate]/total_spend,2)*100)
  output = "Percentage spent by category"
  for i in range(100,-10,-10):
    output += '\n' + f"{i}".rjust(3) + '| '
    for percent in cates_percent.values():
      if percent >= i:
        output += 'o  '
      else:
        output += "   "
  output += "\n    " + '-'*(len(cates_percent.keys())*3+1)
  max_cate_len = max(len(i) for i in cates_percent.keys())
  output += '\n     '
  for i in range(max_cate_len):
    for name in cates_percent.keys():
      if len(name) > i:
        output += name[i] +'  '
      else:
        output += "   "
    if i < max_cate_len-1:
      output += "\n     "
  return output

  Thx for @trsilva32 https://github.com/trsilva32/BudgetApp/blob/main/budget.py