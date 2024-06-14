def task_2(a):
    print("start task_2")
    yield "zilola"
    yield "Hamidova"

def task_3(b):
    print("start task_3")
    yield "barno"
    yield "musayeva"


def task_4(a, b):
    print("start task_4")
    yield "abror"
    yield "odilov"


def test():
    yield task_2(2)
    yield task_3(2)
    yield task_4(2, 3)

for i in test():
    print("next")
    for j in i:
        print(j)
