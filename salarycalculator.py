class Salary:
    def __init__(self,basic):
        self._basic = basic
    def basicSalary(self):
        return float(self._basic)
class Deductions(Salary):
    def __init__(self,pf,insurance):
        self._pf = pf
        self._insurance = insurance
    def calcdeductions(self):
        totalDuct=0
        totalDuct += float(self._pf) * super().basicSalary()
        totalDuct += float(self._insurance)
        return totalDuct

class Allowances(Salary):
    def __init__(self, hra,da,ta):
        self._hra = hra
        self._da = da
        self._ta = ta
    def calcallowance(self):
        totalallowance=0
        totalallowance += float(self._hra)*super().basicSalary()
        totalallowance += float(self._da) * super().basicSalary()
        totalallowance += float(self._ta) * super().basicSalary()
        return totalallowance
class PofessionalTax(Allowances):
    def __init__(self, basic):
        self._basic = basic
    def calcprofessional(self):
        gsal=0
        totalprof=0
        gsal=super().basicSalary()+super().calcallowance()
        if(gsal >=8500 and gsal <=10000):
            totalprof=200
        elif (gsal >= 10000 and gsal <= 30000):
            totalprof = 300
        elif(gsal >= 30000):
            totalprof = 500
        return totalprof


class CalculateSalary(Deductions,PofessionalTax):
    def __init__(self, basic):
        self._basic = basic
    def calcTotalsalary(self):
        super().basicSalary()
        print("Deductions",super().calcdeductions())
        print("Allowances", super().calcallowance())
'''e1=Salary(3000)
e1.basicSalary()
e2=Deductions(0.2,1200)
e2.calcdeductions()
e3=Allowances(0.5,.3,0.15)
e3.calcallowance()'''
e3=CalculateSalary()
e3.calcTotalsalary()



