import pyodbc


def table():
    connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL '
                             "Server};SERVER=LAPTOP-SF1OAQA1;"
                             'Database=Game;'
                             'Trusted_Connection=yes;')

    # query = "CREATE TABLE History_Questions(Q_Number int primary key, Question varchar(200), A varchar(50), B varchar(50), " \
    #          "C varchar(50), D varchar(50), Answer varchar(50)) "
    # cursor = connect.cursor()
    # cursor.execute(query)
    # connect.commit()


table()


def question_input():
    connect = pyodbc.connect('Driver={ODBC Driver 17 for SQL '
                             "Server};SERVER=LAPTOP-SF1OAQA1;"
                             'Database=Game;'
                             'Trusted_Connection=yes;')
    cursor = connect.cursor()

    Q_Number = input("Question_number  ")
    Question1= input("Questions?  ")
    A = input("Choice A  ")
    B = input("Choice B  ")
    C = input("Choice C  ")
    D = input("Choice D  ")
    Answer = input("The answer ")
    cursor.execute("INSERT INTO History_Questions(Q_Number,Question,A,B,C,D,Answer)"
                   "VALUES(?,?,?,?,?,?,?)", (Q_Number, Question1, A, B, C, D, Answer))
    connect.commit()


question_input()
