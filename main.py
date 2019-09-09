class Person(object):
    def __init__(self,no,name,time,TakeOff):
        #従業員の番号、あんまり必要ないかも？
        self.no = no
        self.name = name
        #出勤の時間帯、0が朝、１が昼、２が夜
        self.time = time
        #希望休
        self.TakeOff = TakeOff
    
    def get_TakeOff(self):
        return self.TakeOff
    
    def get_time(self):
        return self.time

def main():
    #従業員の情報
    e0 = Person(0,"mg",[0,1],[23,30,20])
    e1 = Person(1,"mi",[0],[25,4])
    e2 = Person(2,"sm",[0,1],[])
    e3 = Person(3,"nd",[0,1],[])
    e4 = Person(4,"ms",[0],[29,5,20])
    e5 = Person(5,"me",[2],[22,23,27,30,31,1,2,3,4,5,6,7])

    employees = [e0,e1,e2,e3,e4,e5]

    print(employees[5].get_TakeOff())

if __name__ == '__main__':
    main()