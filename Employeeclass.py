import datetime
today = datetime.date.today()
year=today.year
print(year)
class Company:
    def __init__(self,cname):
        self._cname=cname
    def displayCname(self):
        print("Company Name:",self._cname)
    def address(self):
        return ("Technopark Phase 2 Trivandrum");
"""c1.company("UST")
c2.company("BMW")
c1.displayCname()
c2.displayCname()"""
class Employee(Company):
   isMarried=True
   empcount=0
   def __init__(self,fname,lastname,designation,yob):
     self._fname =fname;
     self._lname =lastname;
     self._designation =designation;
     self._yob =yob;
     Employee.empcount+=1
   def getemployeeDetails(self):
      print("fullname",self._fname,"",self._lname)
      print("yob",self._yob)
      print("Designation",self._designation)
      print("Marrital status", self.isMarried)
      print("Employee Count", self.empcount)
   def address(self):
       print("company address", super().address())
       print("Employer address:ust global trivandrum")
e1 = Employee("ee","eeeerty","head",1987)
e1.isMarried=False
e1.empcount=8;
e2 = Employee("ee2","tesr","EUhead",1986)
e1.getemployeeDetails()
e2.getemployeeDetails()
e1.address()
