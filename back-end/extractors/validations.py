class Validations:

    def isValidPhoneNum(self, num):
        check = 0
        for n in num:
            if n.isdigit():
                check += 1

        return (num != None) & (check >= 9)
    
    def isValidString(self, nombre):
        return (nombre != None) & (len(nombre) > 0)
    
    def isValidPostalCode(self, postCode):
        return (postCode != None) & (len(postCode) == 5)

