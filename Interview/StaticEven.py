class EvenNumber:
    @staticmethod
    def Even(n):
        if n%2==0:
            return "the given number is even number"
        else:
            return "the given number is odd number"
print(EvenNumber.Even(8))
