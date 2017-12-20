from db_actions import mongoActions

dba = mongoActions('users')
options = {'1':dba.insertUser,'2':dba.showAllUsers,'3': dba.deleteUser, '4':dba.countUsers,'5':dba.showUser,'6':dba.dropCollection}

def main():
    try:
        while True:
            print("\nSelect 0 to Exit")
            for key,value in options.items():
                print('Select {0} to {1}'.format(key, value.__doc__))

            choose = input("\nWhat do you want to do ? ")
            if choose =='0':
                exit()
            options[choose]()
    except Exception as e:
        print(e)

if __name__ == "__main__":

    if dba.getConnection():
        print("Connection established!")
        main()
    else:
        print("Error to connect MongoDB. Is the server up ?")
