class PrimeNumber:
    def __init__(self, quantity):
        self.quantity = quantity

    def __getitem__(self):

        quantity = self.quantity
        current_position = 1
        current_number = 2
        d = 0
        pnList = []

        while current_position <= quantity:

            for i in range(2, current_number):

                if current_number % i == 0:
                    d += 1

            if d == 0:
                pnList.append(current_number)
                current_position += 1
            else:
                d = 0

            current_number += 1

        else:
            return pnList

#example = PrimeNumber(100)
#print(example.__getitem__())
