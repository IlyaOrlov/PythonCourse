class Man:

    def __init__(self, first_name):
        self.first_name = first_name

    def solve_task(self):
        print("'I`m not ready yet'")


man = Man("Deadpool")
print(f"{man.first_name}:", end = " ")
man.solve_task()
