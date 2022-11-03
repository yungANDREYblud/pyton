class Polindrom():
    def __init__(self, str):
        self.str = str


    def dlina_stroki(self):
        return len(self.str)

    def reverse_stroka(self):
        end = len(self.str)
        st = ""
        for i in range(end-1, -1, -1):
            st += self.str[i]
        return st

    def poli(self):
        if self.str == self.reverse_stroka():
            print("Polidrom")
        else:
            print("Ne Polidrom")

stroka = input()
stroka1 = Polindrom(stroka)
stroka1.poli()
