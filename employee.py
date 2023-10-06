"Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryType, commisionType = None):
        self.name = name
        self.salaryType = salaryType[0]
        self.salaryAmount = salaryType[1]

        if salaryType[0] == "contract":
            self.hours = salaryType[2]

        if (commisionType != None):
            if commisionType[0] == "commission for contracts":
                print("hi")
                self.commisionType = commisionType[0]
                self.commissionRate = commisionType[1]
                self.contractNum = commisionType[2]
            elif commisionType[0] == "bonus commission":
                self.commisionType = commisionType[0]
                self.commissionBonus = commisionType[1]
        else:
            self.commisionType = None
    def get_pay(self):
        totalPay = 0
        if self.salaryType == "monthly salary":
            totalPay += self.salaryAmount
            if self.commisionType != None:
                if self.commisionType == "commission for contracts":
                    totalPay += self.contractNum * self.commissionRate
                elif self.commisionType == "bonus commission":
                    totalPay += self.commissionBonus
        elif self.salaryType == "contract":
            totalPay += self.salaryAmount * self.hours
            if self.commisionType != None:
                if self.commisionType == "commission for contracts":
                    totalPay += self.contractNum * self.commissionRate
                elif self.commisionType == "bonus commission":
                    totalPay += self.commissionBonus
        return totalPay


    def __str__(self):
        explanatoryText = ""
        if self.salaryType == "monthly salary":
            explanatoryText = f"{self.name} works on a {self.salaryType} of {self.salaryAmount}"
        elif self.salaryType == "contract":
            explanatoryText = f"{self.name} works on a {self.salaryType} of {self.hours} hours at {self.salaryAmount}/hour"
        if self.commisionType != None:
            if self.commisionType == "commission for contracts":
                explanatoryText += f" and receives a commission for {self.contractNum} contract(s) at {self.commissionRate}/contract"
            elif self.commisionType == "bonus commission":
                explanatoryText += f" and receives a bonus commission of {self.commissionBonus}"
        explanatoryText += f".  Their total pay is {self.get_pay()}."
        return explanatoryText


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ['monthly salary', 4000])

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ['contract', 25, 100])

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',  ['monthly salary', 3000], ['commission for contracts', 200, 4])

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ['contract', 25, 150],  ['commission for contracts', 220, 3])

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',  ['monthly salary', 2000], ['bonus commission', 1500])

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ['contract', 30, 120],  ['bonus commission', 600])