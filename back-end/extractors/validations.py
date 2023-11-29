class Validations:

    def isValidPhoneNum(self, num):
        return (num != None) & (len(num) == 9)
    
    def isValidString(self, nombre):
        return (nombre != None) & (len(nombre) > 0)
    
    def isValidPostalCode(self, postCode):
        return (postCode != None) & (len(postCode) == 5)

