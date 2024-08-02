def displaymenu():
    print("1. View the store\n")
    print("2. Purchase the item\n")
    print("3. Update the purchase item\n")
    print("4. Remove the item\n")
    print("5. View the purchased item list\n")
    print("6. Exit and Generate Invoice\n")
def storelisting():
    for items in s_store:
        print("\nItem Id : ",items["ItemId"])
        print("\nItem Name : ",items["ItemName"])
        print("\nItem Price : ",items["ItemPrice"])
    runall()
def purchaseitem():
    itemvalue =int(input("Please Enter Itemid"))
    quantity = int(input("Please Enter quantity"))

    if(type(itemvalue) is   int):
        count=0
        for item in s_store:
            if item["ItemId"] == itemvalue:
                cost=item["ItemPrice"]*int(quantity)
                p_purchase.append({"ItemId":itemvalue,"ItemName":item["ItemName"],"ItemPrice":item["ItemPrice"],"ItemQuantity":quantity,"cost":cost})
                count += 1
                addnew= input("Do you want to purchase more items?(Y/N)")
                if addnew.lower() =='y':
                    purchaseitem()
                elif addnew.lower() =='n':
                    runall()
        if count ==0:
            print("Item Id is Not in the Store")
        runall()
    else:
        print("Item Id is not in the Store", itemvalue)

def updatePurchasedata():
    data_input = int(input("Enter the ItemID to Modify"))
    if (type(data_input) is int):
        updateCounter=0
        for data in p_purchase:
            if data["ItemId"] == data_input:
                print("Not a number", data["ItemId"])
                print('Enter the Item Quantity of ',data["ItemName"],'from Purchased records'  )
                data_quantity = float(input())
                print('Enter the Item Price of ', data["ItemName"], 'from Purchased records')
                data_price = float(input())
                data["ItemPrice"] =data_price
                data["ItemQuantity"] = data_quantity
                data["cost"] = data_price*data_quantity

                updateCounter +=1
                if updateCounter < 0:
                    break

            else:
                print(" Item Id is not in the Store")
        runall()
    else:
        print(" Item Id is not a Number.Please enter combination of Numbers from 1 to 10")


def  removeItemsfromcart():
    itemId =int(input("Enter the Item Id to remove"))
    for items in range(len(p_purchase)):

        if p_purchase[items]['ItemId'] == itemId:
            del p_purchase[items]
            break
    runall()
    print(p_purchase)
def  displayItemsfromcart():

    for items in range(len(p_purchase)):
        print(p_purchase[items]['ItemName']," ",p_purchase[items]['ItemPrice']," ",p_purchase[items]['ItemQuantity']," ",p_purchase[items]['cost'])

    runall()
def generateinvoice():

    totalsum = 0
    with open("invoices.txt", "w") as f:
        f.write("************ Invoice Copy ********************\n")
        for items in range(len(p_purchase)):
            totalsum += p_purchase[items]['cost']
            f.write(f"\n{p_purchase[items]['ItemName']}    {p_purchase[items]['ItemName']}     {p_purchase[items]['ItemPrice']}       {p_purchase[items]['ItemQuantity']}           {p_purchase[items]['cost']}")
            f.write(f"\n------------------------------------------------------------------------------------")

        f.write(f"\n                        Total amount:: {totalsum}")

    runall()
def runall():
    displaymenu()
    option = int(input("Please Enter any of options from above menu"))
    if(option == 1):
        storelisting()
    elif(option == 2):
       purchaseitem()
    elif (option == 3):
       updatePurchasedata()
    elif (option == 4):
        removeItemsfromcart()
    elif (option == 5):
        displayItemsfromcart()
    elif (option == 6):
       generateinvoice()
s_store =[{"ItemId":101,"ItemName":"Bat","ItemPrice":1500},{"ItemId":102,"ItemName":"Ball","ItemPrice":100},{"ItemId":103,"ItemName":"Stumps","ItemPrice":500},{"ItemId":104,"ItemName":"Wickets","ItemPrice":150},{"ItemId":105,"ItemName":"Gloves","ItemPrice":800},{"ItemId":106,"ItemName":"Cap","ItemPrice":250}]
p_purchase = []
runall()



