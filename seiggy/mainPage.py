
import time                    #Deltatime library, to get Real Date information.
import threading

class Swiggy():
    print("\n" * 5)                #Starting after 5x empty lines.
    def __init__(self): 
        
        self.restaurant_dict = {"SHAAM E KHAAS":0, "SPICE WORLD":0, "BASKIN ROBBINS":0,"CHATORI GALI":0,"HYDERABADI BIRYANI":0}  #Dictionary of Restaurants
        self.menu_restaurant = {
                "SHAAM E KHAAS" : {"PANEER LABABDAR":250, "PANEER DO PYAZA":300, "VEG MANCHURIAN DRY ":250,\
                    "PANEER CHILLI      ":255, "FRUIT CUSTARD   ":200},\
                "SPICE WORLD" : {"CHEESE FINGERS" : 199,"VEGGIE PIZZA" : 300, "HAKKA NOODLES" : 220,\
                    "STUFFED KULCHA" : 69, "CHESSE CAKE " : 149},\
                "BASKIN ROBBINS" : {"HOT AND SOUR     ":109, "BABY CORN      ":219, "MASALA DOSA   ":300, "CHILLY POTATO  ":219,\
                    "CLUB SANDWICH":250},\
                "CHATORI GALI" : {"VEG KADAI     ":190, "PANEER TIKKA":260, "JEERA RICE  ":150, "SOYA CHAAP    ":180,\
                    "CHICKEN LOLLIPOP":350},\
                "HYDERABADI BIRYANI" : {"VEG DUM BIRYANI ": 150, "PANEER BIRYANI ":300,"CHICKEN BIRYANI":300,"EGG BIRYANI  ":200}
                }
        self.auth = {"SHAAM E KHAAS" : {"mayur":123},\
                "SPICE WORLD" : {"manasa":123},\
                "BASKIN ROBBINS" : {"chandra":123},\
                "CHATORI GALI" : {"amit":123},\
                "HYDERABADI BIRYANI":{"abc":123}}
                
    def mainMenu(self):
        while True:                                                 #Repeat Menu until stops.
            print("\n")
            print(">" * 36 + "WELCOME TO SWIGGY" + "<" * 36 )       
            print("\n"*2)
            print(">" * 36 + "MAIN MENU" + "<" * 36 + "\n"              #Design for Main Menu
                    "\t(O) ORDER FOOD\n"                                #"*" * 31 means, write (*) 31 times.
                    "\t(J) OTHER SERVICES\n"
                    "\t(E) EXIT\n"+
                    "-" * 89)

            input_1 = str(input("PLEASE SELECT YOUR OPERATION: ")).upper()   #Input, have to choose operation. Make everything UPPER symbol.
            if (input_1 == "O"):                                             #If input is 'O'
                #print("\n" * 10) 
                self.orderFood()                                              #Start Order Menu function.
                break
            elif (input_1 == "J"):                                           #If input is 'J'
                print("\n" * 10) 
                self.joinServices()
            elif (input_1 == "E"):
                print(">" * 36 + "THANK YOU" + "<" * 36 + "\n")             #Good bye comment.
                break
            else:
                print("\n" + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") #Invalid input.

    def orderFood(self):                                                    # While looping to keep menu alive
        while True:
            print("\n" * 1)
            print(">" * 36,"ORDER FOOD","<" * 36)
            print("PLEASE SELECT THE RESTAURANT OF YOUR CHOICE: \n")        #Selecting the restaurant
            
            for i in range (0,len(self.restaurant_dict)):                   #Iterating over the list
                print("(",i+1,")"," ",(list(self.restaurant_dict.keys())[i]),sep='')
                print()
            print()
            print("(M) BACK TO MAIN MENU","\t" * 5,"(S) SEARCH FOR DISH / RESTAURANT") 
            print("-" * 89)
            input_2 = input("PLEASE SELECT YOUR OPERATION: ")              #Options Handling

            input_check = []
            if input_2.upper() == "M":                                     #If input is 'M'
                self.mainMenu()                                             #Back to main menu
                break
            elif input_2.upper() == "S":                                   #If input is 'S'
                print("\n" * 2)
                self.search_item()                                      #go to Search Menu
                break    
            elif input_2 != "M" and input_2 != "S":
                for i in input_2:
                    if ord(i) >= 48 and ord(i) <= 57:
                        input_check.append("True")
                    else:
                        input_check.append("False")
            if "False" in input_check:
                print("\n" + "ERROR: Invalid Input (",input_2,"). Try again!",sep='')  # Handling Bad Inputs
            else:
                input_2 = int(input_2)
                if input_2 <= len(self.restaurant_dict): 
                    self.restaurant_menu(list(self.restaurant_dict.keys())[input_2-1])
                    break       
                else:
                    print("\n" + "ERROR: Invalid Input (",input_2,"). Try again!",sep='')  # Handling Bad Inputs
    
    def restaurant_menu(self,res):
        if self.restaurant_dict[res] > 2:
            print("SORRY WE ARE CURRENTLY NOT ACCEPTING ANY ORDERS FOR THIS RESTAURENT!")
            self.orderFood()
        else:
            dish_input_food_list = []
            dish_input_price_list = []
            dish_quantity_list = []
            while True:
                print("\n"*2)
                print(">"*34,"MENU OF",res,"<"*34)
                print("\n"*2)
                if res in self.menu_restaurant:
                    print("ITEMS","\t"*9,"PRICE")
                    print("-"*89)
                    i = 0
                    for k,v in self.menu_restaurant[res].items():
                        i += 1
                        print("(",i,")"," ",k,"\t"*7,v,sep="")
                    print("-"*89)
                    print("(V) VIEW CART","\t"*7,"(B) BACK TO ORDER FOOD PAGE")
                    print("-"*89)
                    dish_input = input("PLEASE SELECT DISH OF YOUR CHOICE: ")
                num_input_check = []
                if dish_input.upper() == "B":
                    self.orderFood()
                    break
                elif dish_input.upper() == "V":
                    print("\n"*2)
                    print(">"*39,"YOUR CART","<"*39)
                    if dish_input_food_list != [] and dish_input_price_list != [] and dish_quantity_list != []:
                        self.cart(dish_input_food_list,dish_input_price_list,dish_quantity_list,res)
                        break
                    else:
                        print("\n"*2)
                        print("\t"*4,"YOUR CART IS EMPTY!!")
                        continue
                elif dish_input != "V" or dish_input != "B":
                    for i in dish_input:
                        if ord(i) >= 48 and ord(i) <= 57:
                            num_input_check.append("True")
                        else:
                            num_input_check.append("False")
                    if "False" in num_input_check:
                        print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='')
                    else:
                        food_and_price_list = []
                        dish_input = int(dish_input)
                        if dish_input <= len(self.menu_restaurant[res].items()):
                            try:
                                dish_quantity = int(input("PLEASE SELECT THE QUANTITY FOR THE DISH SELECTED: "))
                                dish_quantity_list.append(dish_quantity)
                            except Exception:
                                print("\n" + "ERROR: Invalid Input. Try again!")
                                continue
                            print("\n"*2)
                            for food,price in self.menu_restaurant[res].items():
                                food_and_price_list.append(food)
                                food_and_price_list.append(price)
                            dish_input_food_list.append(food_and_price_list[(dish_input)*2-2])
                            dish_input_price_list.append(food_and_price_list[dish_input*2-1])
                            # print(dish_input_food_list)
                            # print(dish_input_price_list)
                            print(">"*34,"TEST","<"*34)
                            print("\n"*2)     
                        else:
                            print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='')
                else:
                    print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='')
    
    def cart(self,dish_input_food_list,dish_input_price_list,dish_quantity_list,res):
        while True:
            total_price = []
            j = 0
            while j < len(dish_input_price_list):
                total_price.append((dish_quantity_list[j])*(dish_input_price_list[j]))
                j += 1
            print("\n")
            print("-"*89)
            print("ITEMS","\t"*5,"QUANTITY","\t"*4,"PRICE")
            print("-"*89)
            i = 0
            sr_no = 1
            while i < len(dish_input_food_list):
                print("(",sr_no,")"," ",dish_input_food_list[i],"\t","*","\t"*2, dish_quantity_list[i],\
                    "\t"*5,total_price[i],sep="")
                i += 1
                sr_no += 1
            print("-"*89)
            print("TOTAL","\t"*10,sum(total_price))
            if sum(total_price) >= 3500:
                print("DISCOUNT RECEIVED","\t"*3,"15%","\t"*5,"-",(15*(sum(total_price))/100),sep="")
                discount_total_price = float(sum(total_price)) - (15*(sum(total_price))/100)
                print("TOTAL","\t"*10,(discount_total_price))
            print("-"*89)
            print("(P) PAYMENT","\t"*8,"(B) BACK TO MENU")
            print("-"*89)    
            cart_input = input("PLEASE SELECT YOUR OPERATION: ")
            if cart_input.upper() == "B":
                self.restaurant_Menu(res)
                break
            elif cart_input.upper() == "P":
                self.payment(res)
                break
            else:
                print("\n" + "ERROR: Invalid Input (",cart_input,"). Try again!",sep='')


    def payment(self,res):
        while True:
            print("\n")
            print(">"*39,"PAYMENT","<"*39)
            print("\n")
            print("SR NO","\t"*2,"MODES OF PAYMENT")
            print("-"*89)
            print("(1)","\t"*2,"CREDIT CARD")
            print("(2)","\t"*2,"DEBIT CARD")
            print("(3)","\t"*2,"NET BANKING")
            print("(4)","\t"*2,"UPI PAYMENT")
            print("-"*89)
            print("(C)","\t"*2,"CANCEL PAYMENT")
            print("-"*89)
            payment_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
            if payment_input == "C":
                self.restaurant_Menu(res)
                break
            elif payment_input == "1" or payment_input == "2" or payment_input == "3" or payment_input == "4":
                self.restaurant_dict[res] += 1
                self.payment_Status(res)
                break
            else:
                print("\n" + "ERROR: Invalid Input (",payment_input,"). Try again!",sep='')


    def payment_Status(self,res):
        self.queueList = []
        while True:
            print("\n")
            print(">"*39,"PAYMENT STATUS","<"*39)
            print("\n"*3)
            print("\t"*4,"PAYMENT SUCCESSFUL")
            print("\n"*3)
            print("-"*89)
            print("(M)","\t","BACK TO MAIN MENU")
            print("-"*89)

            def endHotelProcess(res):
                while(self.restaurant_dict[res]!=0):
                    time.sleep(100)
                    self.restaurant_dict[res] -= 1
            t1 = threading.Thread(target= endHotelProcess,args=(res,))
            self.queueList.append(t1)
            self.queueList[-1].start()
            payment_Status_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
            if payment_Status_input == "M":
                self.mainMenu()
                break
            else:
                print("\n" + "ERROR: Invalid Input (",payment_Status_input,"). Try again!",sep='')



    def joinServices(self):
        while True:
            print("\n")
            print(">"*35,"JOIN OUR SERVICES","<"*35)
            print("\n")
            print("-"*89)
            print("(1) NEW USER")
            print("(2) EXSISTING USER")
            print("\n"*2)
            print("-"*89)
            print("(M) BACK TO MAIN MENU")
            print("-"*89)
            joinServices_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
            if joinServices_input == "M":
                self.mainMenu()
                break
            elif joinServices_input == "1":
                self.new_User()
                break
            elif joinServices_input == "2":
                self.exsisting_User()
                break
            else:
                print("\n" + "ERROR: Invalid Input (",joinServices_input,"). Try again!",sep='')
    def new_User(self):
        while True:
            print("\n")
            print(">"*32,"COMPLETE YOUR REGISTRATION PROCESS","<"*32)
            print("\n")
            print("-"*89)
            print("(J) BACK TO JOIN SERVICES PAGE")
            print("-"*89)
            new_user_id = input("PLEASE ENTER YOUR USERNAME: ")
            new_user_pwd = int(input("PLEASE ENTER YOUR PASSWORD: "))
            new_user_restaurant = input("PLEASE ENTER NAME OF YOUR RESTAURANT OR OPERATION TO BE PERFORMED: ").upper()       
            if new_user_restaurant == "J":
                self.joinServices()
                break
            elif new_user_restaurant not in self.restaurant_dict:
                id_pwd = {}
                id_pwd.setdefault(new_user_id,new_user_pwd)
                self.auth[new_user_restaurant] = id_pwd
                self.restaurant_dict[new_user_restaurant] = 0
                dish_price = {}
                while True:
                    dish = (input("PLEASE ENTER YOUR DISH NAME TO BE ADDED IN MENU: ").upper())
                    price = int(input("PLEASE ENTER THE AMOUNT FOR THE ABOVE DISH: "))
                    print("-"*89)
                    print("(A) ADD MORE ITEMS","\t"*7,"(D) DONE ADDING ITEMS")
                    new_user_add_menu = input("PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
                    dish_price.setdefault(dish,price)
                    self.menu_restaurant[new_user_restaurant] = dish_price
                    if new_user_add_menu == "D":
                        print("\n"*2)
                        print("\t"*3,"DETAILS ADDED SUCCESSFULLY!!")
                        print("\n"*2)
                        self.mainMenu()
                        break
                    elif new_user_add_menu != "A":
                        print("PLEASE ENTER VALID INPUT!!")
            elif new_user_restaurant in self.restaurant_dict:
                print("THE ENTERED RESTAURANT NAME ",new_user_restaurant," ALREADY EXSIST")
            else:
                print("\n" + "ERROR: Invalid Input (",new_user_restaurant,"). Try again!",sep='')

    def exsisting_User(self):
        while True:
            print("\n"*2)
            print(">"*32,"WELCOME TO SWIGGY SERVICES","<"*32)
            print("\n"*3)
            print("-"*89)
            # print("(T) TRY AGAIN","\t"*4,"(M) BACK TO MAIN MENU")
            # print("-"*89)
            exsisting_user_id = input("PLEASE ENTER USERNAME: ")
            exsisting_user_pwd = int(input("PLEASE ENTER PASSWORD: "))
            # exsisting_user_input = input("PLEASE SELECT OPERATION TO BE PERFORMED: ")
            for k,v in self.auth.items():
                if exsisting_user_id in v and exsisting_user_pwd in v.values():
                    self.update_Menu(k)
                    break
            else:
                print("\n" + "ERROR: Incorrect Username or Password entered. Try again!",sep='')

    def update_Menu(self,k):
        while True:
            if k in self.menu_restaurant:
                print(">"*35,"MENU OF",k,"<"*35)
                print("\n")
                print("-"*89)
                print("ITEMS","\t"*9,"PRICE")
                print("-"*89)
                i = 0
                for r,v in self.menu_restaurant[k].items():
                    i += 1
                    print("(",i,")"," ",r,"\t"*7,v,sep="")
                print("-"*89)
                print("(A) ADD NEW DISH","\t"*2,"(M) BACK TO MAIN MENU","\t"*2,"(R) REMOVE DISH")
                print("-"*89)
                update_menu_input = input("PLEASE ENTER DISH NAME TO BE UPDATED OR SELECT ANY OPERATION TO BE PERFORMED: ").upper()                      
                if update_menu_input in self.menu_restaurant[k]:
                    price = input("PLEASE ENTER THE NEW PRICE: ")
                    self.menu_restaurant[k][update_menu_input]=price
                elif update_menu_input == "M":
                    self.mainMenu()
                    break
                elif update_menu_input == "A":
                    self.add_Dish(k)
                elif update_menu_input == "R":
                    self.remove_Dish(k)
                else:
                    print("\n" + "ERROR: Invalid Input (",update_menu_input,"). Try again!",sep='')
            else:
                print("\n" + "ERROR: Incorrect Username or Password entered. Try again!",sep='')

    def add_Dish(self,k):
        while True:
            print("\n")
            print(">"*20,"PLEASE ENTER DETAILS OF YOUR DISH TO BE ADDED","<"*20)
            print("\n"*2)
            print("-"*89)
            dish = (input("PLEASE ENTER YOUR DISH NAME TO BE ADDED IN MENU: ").upper())
            price = int(input("PLEASE ENTER THE AMOUNT FOR THE ABOVE DISH: "))
            if dish not in self.menu_restaurant[k]:
                self.menu_restaurant[k][dish]=price
            print("-"*89)
            print("(A) ADD MORE ITEMS","\t"*6,"(D) DONE ADDING ITEMS")
            add_dish_input = input("PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
            if add_dish_input == "D":
                print("\n"*2)
                print("\t"*3,"DETAILS ADDED SUCCESSFULLY!!")
                print("\n"*2)
                self.update_Menu(k)
                break
            elif add_dish_input != "A":
                print("PLEASE ENTER VALID INPUT!!")

    def remove_Dish(self,k):
        while True:
            print("\n")
            print(">"*20,"PLEASE ENTER NAME OF THE DISH TO BE REMOVED","<"*20)
            print("\n"*2)
            print("-"*89)
            print("(T) TRY AGAIN","\t"*5,"(B) BACK TO UPDATE MENU PAGE")
            print("-"*89)
            dish = (input("PLEASE ENTER YOUR DISH NAME TO BE REMOVED: ").upper())
            if dish in self.menu_restaurant[k]:
                del self.menu_restaurant[k][dish]
                self.update_Menu(k)
                break
            else:
                print("\n" + "ERROR: (",dish,"). not found in Menu. Try again!",sep='')
            print("-"*89)
            remove_dish_input = input("ENTER OPERATION TO BE PERFORMED: ").upper()
            if remove_dish_input == "B":
                self.update_Menu(k)
                break
            elif remove_dish_input != "T":
                print("\n" + "ERROR: Invalid Input (",remove_dish_input,"). Try again!",sep='')

    def search_item(self):
        dish_input_food_list = []
        dish_input_price_list = []
        dish_quantity_list = [] 
        while True:
            cart_dict = {}
            print(">"*43,"SEARCH MENU","<"*43)
            print("\n" * 3)
            print("-"*100)
            print("(V) VIEW CART" ," "*50, "(M) MAIN MENU"," "*30)
            print("-"*100)
            print()
            sec_item = (input("SEARCH YOUR DISS Or CHOOSE OTHER OPTION: ").upper())
            if sec_item == "V":
                self.cart(dish_input_food_list,dish_input_price_list,dish_quantity_list,res)
                break
            elif sec_item == "M":
                self.mainMenu()
                break
            if sec_item != "M" and sec_item != "V":
                a = 0
                for i,j in self.menu_restaurant.items():
                    if i == sec_item:
                        print("\n"*3)
                        print("-"*45, i,"-"*45 )
                        print("\n"*3)
                        for x, y in j.items():
                            a += 1
                            print('(',a,")",x,"\t"*5,y)
                            break
                    for x, y in j.items():
                        b = {}
                        if sec_item in x:
                            a += 1
                            print(i)
                            print("\n")
                            b[x] = y
                            cart_dict[i] = b
                            print("(",a,")",x,(" "*20),"Price: ",y)
                            print('-'*60)
            
            slect_item = int(input("SELECT YOUR CHOISE: ")) 
            a = 0
            for i, j in cart_dict.items():
                for x, y in j.items():
                    a += 1
                    if a == slect_item:
                        res = i
                        try:
                            dish_quantity = int(input("PLEASE SELECT THE QUANTITY FOR THE DISH SELECTED: "))
                            dish_quantity_list.append(dish_quantity)
                        except Exception:
                            print("\n" + "ERROR: Invalid Input. Try again!")
                        dish_input_food_list.append(x)
                        dish_input_price_list.append(y)
                    
                

                

            
                
            



if __name__ == "__main__":
    s=Swiggy()                                   
    s.mainMenu()
    
    
