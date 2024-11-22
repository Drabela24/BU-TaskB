def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    
    if current_day not in range(0,50,7): #Checks if its not a restock day
        pass


    elif current_day in range(0,50,7): #Checksif the current day is a restock day 
        if current_day == 0: #Hard set of restocking on day 0
            restocked_units = 2000
            sold_units = 0 # No sells on restock day
            inventory_records.append([current_day, sold_units, restocked_units, available_items]) #Update inventory
        
        else: #Resrocking day that are not day 0
            restocked_units = 2000 - available_items #Establishing ammount of restocking items needed
            available_items += restocked_units #Restocking the available units bak to full capacity
            sold_units = 0  
            inventory_records.append([current_day, sold_units, restocked_units, available_items])

    elif current_day > 49: 
        quit
        
            
    return available_items

