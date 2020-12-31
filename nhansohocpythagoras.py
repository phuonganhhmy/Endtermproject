import matplotlib.pyplot as plt

class Person:

    def __init__(self, name, middlename, surname, day, month, year):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.vowel = {'A':1, 'U':3, 'E':5, 'O':6, 'Y':7, 'I':9}
        self.consonant = {'J':1, 'S':1, 'B':2, 'K':2, 'T':2, 'C':3, 'D':4, 'M':4, 'V':4, 'N':5, 'W':5, 'F':6, 'X':6, 'G':7, 'P':7, 'H':8,
                        'Q':8, 'Z':8, 'R':9}
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.word = name + middlename + surname
        self.word = list(self.word)
    def Gcal(self):
        # word = list(word)
        total = 0
        for letter in self.word:
            if letter in self.vowel:
                value = self.vowel[letter]
            else:
                value = self.consonant[letter]
            total += value
            total = self.reduce(total)
        return(total)
    def reduce(self, num):
        if num == 11 or num == 22:
            total = num
        elif num%9 == 0:
            total = 9
        else:
            total = num%9
        return(total)
    def soulnumber(self):
        soulnum = 0
        for letter in self.word:
            if letter in self.vowel:
                value = self.vowel[letter]
                soulnum = soulnum + value
                soulnum = self.reduce(soulnum)
        return(soulnum)
    def personalitynumber(self):
        pernum = 0
        for letter in self.word:
            if letter in self.consonant:
                value = self.consonant[letter]
                pernum = pernum + value
                pernum = self.reduce(pernum)
        return(pernum)
    def pathlifenumber(self):
        plnum = day + month + year
        plnum = int(plnum)
        plnum = self.reduce(plnum)
        return(plnum)
    def decrease(self, num):
        total = 0
        if num < 10:
            total = num
        elif num % 9 == 0:
            total = total + 9
        else:
            total = num%9
        return(total)
    def reduc(self, num):
        if num <= 11:
            total = num
        else:
            size = len(str(num))
            num = list(str(num))
            total = 0
            for n in num:
                total = total + int(n)
        return(total)
    def Day(self):
        return self.decrease(self.day)
    def Month(self):
        return self.decrease(self.month)
    def Year(self):
        return self.decrease(self.year)
    def Firstpeak(self):
        MD = self.Day() + self.Month()
        MD = self.decrease(MD)
        return(MD)
    def Secondpeak(self):
        DY = self.Day() + self.Year()
        DY = self.decrease(DY)
        return(DY)
    def Thirdpeak(self):
        MDY = self.Firstpeak() + self.Secondpeak()
        MDY = self.reduc(MDY)
        return(MDY)
    def Finalpeak(self):
        MY = self.Month() +self.Year()
        MY = self.reduc(MY)
        return(MY)
    def process(self):
        first = 36 - self.pathlifenumber()
        second = first + 9
        third = second + 9
        final = third + 9
        return first, second, third, final
    def Bieudonhansinh(self):
        plt.figure()
        plt.axis('off')
        plt.title('bieu do nhan sinh')
        plt.plot([1,3], [1,3])
        plt.plot([3,5], [3,1])
        plt.plot([5,7], [1,3])
        plt.plot([7,9], [3,1])
        plt.plot([3,5], [3,5])
        plt.plot([5,7], [5,3])
        plt.plot([0,5], [1,6])
        plt.plot([5,10], [6,1])
        plt.grid(True)
        plt.show()

class PrintNumber:
    def __init__(self, person):
        self.person = person

    def printNums(self):
        print("Phần tính toán cho tên:", self.person.name, self.person.middlename, self.person.surname)
        print("======================================================================================")
        print("So ung voi ten goi cua ban la:", self.person.Gcal())
        print("Chi so tam hon cua ban:", self.person.soulnumber())
        print("Chi so the hien cua ban la:", self.person.personalitynumber())
        print("--------------------------------------------------------------------------------------")
        print("Phan tinh toan cho ngay sinh cua ba la:", self.person.day,"/", self.person.month,"/",self.person.year)
        print("======================================================================================")
        print("Con so dac biet danh cho ban la ung voi so:", self.person.pathlifenumber())
        first, second, third, final = self.person.process()
        print("Dinh thu nhat trong cuoc doi ban vao nam", first," ung voi so:",self.person.Firstpeak())
        print("Dinh thu hai trong cuoc doi ban vao nam", second, "ung voi so:", self.person.Secondpeak())
        print("Dinh thu ba trong cuoc doi ban vao nam", third, "ung voi so:", self.person.Thirdpeak())
        print("Dinh Thu tu trong cuoc doi ban vao nam", final, "ung voi so:", self.person.Finalpeak())
        self.person.Bieudonhansinh()

incoming = input("hay nhap vao ten day du va sinh nhat cua ban:")
incoming = incoming.upper()
incoming = incoming.split(" ")

name = incoming[0]
middlename = incoming[1]
surname = incoming[2]
day = incoming[3]
month = incoming[4]
year = incoming[5]

person = Person(name, middlename, surname, day, month, year)
calculation = PrintNumber(person)
calculation.printNums()

