import pickle


class SerCls:
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

    def __str__(self):
        return f"SerCls(lst={self.lst}, dct={self.dct}, num={self.num}, st='{self.st}')"


ser = SerCls(lst=[1, 2, 3], dct={"a": 1, "b": 2}, num=42, st="Hello")
print(ser)
serialized_data = pickle.dumps(ser)
del ser
ser1 = pickle.loads(serialized_data)
print(ser1)