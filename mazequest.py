def check_monster(monster_set, maze, stir):
    for i in monster_set:
        if stir == i:
            return "☠"

def level1():
    maze_1 = [["🤍", "🤍", "🤍", "🤍"], ["🤍", "🤍", "🤍", "🤍"], ["🤍", "🤍", "🤍", "🤍"], ["🤍", "🤍", " ", "🤍"]]
    moves = 10
    health = 3
    row = 0
    column = 0
    moves_pic = "⭐"
    health_pic = "💜"
    monster_set_1 = {"03": "", "12": "", "23": "", "31": "", "44": ""}

    print("Welcome to Level 1. Try reaching the bouquet with limited moves you have. BUT! Beware, there are monsters in between your path.")
    print("Tip: Encountering a monster moves you back to the previous position.")

    for i in range(moves):
        print("health = " + health_pic * health)
        print("moves = " + moves_pic * (moves - i))
        position = (row, column)
        for q in range(len(maze_1)):
            for w in range(len(maze_1[q])):
                new_tuple = (q, w)
                if new_tuple == position:
                    maze_1[q][w] = "💙"
        for z in maze_1:
            print(" ".join(z))
        if health < 0:
            print("You are out of lives")
            break

        x = str(input("Enter your move: "))
        print("___\n")

        if x == "right":
            column += 1
            if column > 3 or column < 0:
                print("You are facing the wall")
                column -= 1
            stir = str(row) + str(column)
            y = check_monster(monster_set_1, maze_1, stir)
            if y == "☠":
                print("You have met death")
                health -= 1
                column -= 1
            elif position == (2, 2):
                return "You won!!!!!!!!"

        elif x == "left":
            column -= 1
            if column > 3 or column < 0:
                print("You are facing the wall")
                column += 1
            stir = str(row) + str(column)
            y = check_monster(monster_set_1, maze_1, stir)
            if y == "☠":
                print("You have met death")
                health -= 1
                column += 1
            elif position == (2, 2):
                return "You won!!!!!!!!"

        elif x == "up":
            row -= 1
            if row > 3 or row < 0:
                print("You are facing the wall")
                row += 1
            stir = str(row) + str(column)
            y = check_monster(monster_set_1, maze_1, stir)
            if y == "☠":
                print("You have met death")
                health -= 1
                row += 1
            elif position == (2, 2):
                return "You won!!!!!!!!"

        elif x == "down":
            row += 1
            if row > 3 or row < 0:
                print("You are facing the wall")
                row -= 1
            stir = str(row) + str(column)
            y = check_monster(monster_set_1, maze_1, stir)
            if y == "☠":
                print("You have met death")
                health -= 1
                row -= 1
            elif position == (2, 2):
                return "You won!!!!!!!!"
        else:
            print("The input only accepts up, down, left, and right")

def level2():
    # Similar structure to level1 but with larger maze and more monsters

def level3():
    # Similar structure to level2 but with even larger maze and more monsters

def main():
    print("Welcome to MazeQuest: Bouquet Pursuit. In this game your only target is to reach the bouquet.")
    print("However, there are monsters in the way trying to protect the bouquet from the undeserving. Be Careful!")
    answer = str(input("DO YOU DESERVE THE PRETTY BOUQUET?"))
    if answer.upper() == "YES":
        if level1() == "You won!!!!!!!!":
            print("Congratulations!! You have cleared level 1")
        if level2() == "You won Level 2!":
            print("Congratulations!! You have cleared level 2")
        if level3() == "Congratulations! You completed Level 3 and the entire game!":
            print("CONGRATULATIONS, for believing in yourself!!")
main()
