import random
def main():
    rlist = ["r", "p", "s"]
    welcome = """welcome to rps choose rock, paper or scissors"""
    print(welcome, "\n", "enter r for rock, p for paper, s for scissors")
    p1 = input("enter here: ")
    p2 = random.choice(rlist)
    winner = "player1 win"
    if p1 == p2:
        print("draw")
        main()
    if p1 == "r" and p2 == "s":
        print(winner)
    if p1 == "p" and p2 == "r":
        print(winner)
    else:
        print(winner)
main()
