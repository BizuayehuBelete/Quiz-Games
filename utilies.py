from colorama import Fore, Style
# import color
import pyodbc

class trivia_game():
    def game_1(self):
        print(Fore.LIGHTBLUE_EX+  '\n\t\t\t\t\t .......WELCOME TO TRIVIA GAME......\n' + Fore.RESET)
class Game() :
    def game(self):
        self.user = int(input(Fore.LIGHTBLUE_EX+ "\t\t\t\t\t\t...Please Choose The Catagories.....\n\n" + Fore.RESET +
                         Fore.LIGHTRED_EX+'\t\tEnter 1 for Computer Questions \t\t'+ Fore.RESET +
                         Fore.LIGHTRED_EX +'Enter 2 for History Questions\n\n' + Fore.RESET +
                         Fore.LIGHTRED_EX+ '\t\t\t\t\t\t\tEnter 3 for Sport_Questions \n'+ Fore.RESET ))

        if self.user == 1:
            self.connect = pyodbc.connect('Driver={SQL Server};'
                                      'Server=LAPTOP-SF1OAQA1;'
                                      'Database=Game;'
                                      'Trusted_Connection=yes;')

            X = 'SELECT Question,A,B,C,D ,Answer FROM dbo.Computer_questions'
            self.cursor = self.connect.cursor()
            self.cursor.execute(X)
            score = 0
            for i in self.cursor:
                print(i[0])
                print("A.", i[1], "\n", "B.", i[2], "\n", "C.", i[3], "\n", "D.", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "Choose the best  answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/5")


        elif self.user == 2:
            Sports = pyodbc.connect('Driver={SQL Server};'
                                    'Server=LAPTOP-SF1OAQA1;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')

            Y = 'SELECT Question,A,B,C,D ,Answer FROM dbo.History_Questions'
            cursor = Sports.cursor()
            cursor.execute(Y)
            score = 0
            for i in cursor:
                print(i[0])
                print("A.", i[1], "\n", "B.", i[2], "\n", "C.", i[3], "\n", "D.", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "  Choose the  best answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/5")


        elif self.user == 3:
            self.connect = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-SF1OAQA1;'
                                   'Database=Game;'
                                   'Trusted_Connection=yes;')

            Z = 'SELECT Question,A,B,C,D ,Answer FROM dbo.Sport_Questions'
            self.cursor = self.connect.cursor()
            self.cursor.execute(Z)
            self.score = 0
            for i in self.cursor:
                print(i[0])
                print("A.", i[1], "\n", "B.", i[2], "\n", "C.", i[3], "\n", "D.", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "  Choose the  best answer:" + Fore.RESET)
                if Answer == i[5]:
                    self.score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", self.score, "/5")
        a=input("\u001b[34m\u001b[1m Do you want to Continue?  y/n")
        if a=="y":
            result1 = Game()
            result1.game()
        else:
            exit()







