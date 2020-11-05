import time
import turtle as tr
tr.tracer(False)


def lsystem(axioms, rules, iterations):
    for i in range(iterations):
        newAxioms = ''
        for axiom in axioms:
            if axiom in rules:
                newAxioms += rules[axiom]
            else:
                newAxioms += axiom
        axioms = newAxioms
    return axioms


def funcF():
    tr.forward(3)


def funcG():
    tr.forward(3)


def func_plus():
    tr.right(120)


def func_minus():
    tr.left(120)


tr.penup()
tr.goto(-300, -300)
tr.pendown()
n = 10
func = {"F": funcF, "G": funcG, "+": func_plus, "-": func_minus}
rules = {"F": "F-G+F+G-F", "G": "GG"}
str = lsystem('F-G-G', rules, n)
print(str)
for symbol in str:
    func[symbol]()
print(str)
tr.exitonclick()