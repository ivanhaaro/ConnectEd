class Validations:

    def isValidPhoneNum(self, num):
        return (num != None) and (len(num) == 9)

    def isValidString(self, nombre):
        return (nombre != None) and (len(nombre) > 0)

    def isValidPostalCode(self, postCode):
        return (postCode != None) and (len(postCode) == 5)

    def isAlicante(self, postCode):
        return (postCode != None) and (len(postCode) == 4) and (postCode[0] == '3')
