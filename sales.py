import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
     
    if current_day in range(0,50,7): # Checks if current day it's a restock day
        pass
               
    elif current_day not in range(0,50,7) : #Checks if current day it's not a restock day
            sold_units = random.randint(0,201) # Random number of sales generator
            available_items -= sold_units #Substracting sales from available items accordingly
            restocked_units = 0 #No restocking on sale days
            inventory_records.append([current_day, sold_units, restocked_units, available_items]) #Keeping inventory updated
 
    elif current_day > 49: 
        quit

    return available_items
  
