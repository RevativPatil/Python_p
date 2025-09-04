class Bank:
  roi=7.8

  def _init__(self):
     print("I am Parent's Constructor")
  def setRoi():
     print("ROI applied")
class SavingA(Bank):
  def openA():
     print("Account Opening Process Completed")
class CurrentA(Bank):
  def _init__(self):
     super().__init() #calling Parent's Constructor
     print("I am Child's Constructor")
  def openAc(self):
     print("Account Opening Process Completed")
c1=CurrentA()