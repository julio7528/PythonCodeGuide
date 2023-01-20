import sqlite3
import os

try:
    dbLocation = r'C:\\Users\\julio\\Desktop\\python\\pythonLanScript\\PythonLanScript\\meu_banco_de_dados.db'
    dbTable = 'Customers'

    class Customer:
        def __init__(self,dbLocation):        
            self.dbLocation = dbLocation
            self.conn = None

        def connectDataBase(self):
            self.conn = sqlite3.connect(self.dbLocation)
            print("Connected to the database")

        def insertDataBase(self, customerAge, customerName):
            self.connectDataBase()
            self.conn.execute(f"INSERT INTO {dbTable} (age, name) VALUES ({customerAge}, '{customerName}')")
            self.conn.commit()
            print("Inserted into the database")
            self.closeDataBase()

        def reportDataBase(self):
            self.connectDataBase()
            cursor = self.conn.execute(f"SELECT * FROM {dbTable}")
            self.conn.commit()
            result = cursor.fetchall()
            for row in result:
                print(row)
            print("Selected from the database")
            self.closeDataBase()
            cursor = None

        def selectByName(self, customerName):
            self.connectDataBase()
            cursor = self.conn.execute(f"SELECT * FROM {dbTable} WHERE name = '{customerName}'")
            self.conn.commit()
            result = cursor.fetchall()
            for row in result:
                print(row)
            print("Selected from the database")    
            cursor = None   
            
        def closeDataBase(self):
            self.conn.close()
            print("Closed to the database")
            

    class Person:
        
        def __init__(self):
            self.customerName = ""
            self.customerAge = 0 
            self.option = '0'           

        def insert_Name_Age(self):
            self.customerName = input("Insert the Name: ")
            self.customerAge = input("Insert the Age: ")

        def clearScreen(self):
            os.system('cls' if os.name == 'nt' else 'clear')

        def menu(self):            
            option = self.option               
            while option != '4':
                
                print("1 - Insert a new costumer")
                print("2 - List all costumers")
                print("3 - List costumer by name")
                print("4 - Exit")             
                option = input("Choose an option: ")
                if option == '1':
                    self.clearScreen()
                    print("Type Name of costumer")
                    self.insert_Name_Age()
                    custumer.insertDataBase(self.customerAge, self.customerName)
                elif option == '2':
                    self.clearScreen()
                    print("List of all costumers")
                    custumer.reportDataBase()
                elif option == '3':    
                    self.clearScreen()                
                    customerName = input("Insert the Name: ")
                    print(f"List costumer by name: {customerName}")
                    custumer.selectByName(customerName)
                elif option == '4':
                    self.clearScreen()
                    print("Exit")

    person = Person()
    custumer = Customer(dbLocation)    

    person.menu()    

except Exception as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("Keyboard Interrupt")
except:
    print("Unexpected error")