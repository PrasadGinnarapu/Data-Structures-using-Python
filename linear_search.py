def locate_card(query,cards):
    #variable for position
    position = 0
    
    while position< len(cards):
        
        #Check if element at the current position 
        if cards[position] == query:
            
            #Answer found! Return and exit
            return position
        
        #Increment the position
        position += 1
        
        #Check if we have reached the end of the array
        # if position == len(cards):
            #Number not found, return -1
    return -1
        
cards = [1,2,3,4,5,6]
print(locate_card(int(input('Enter Query: ')),cards))

#Note: 
#Time complexity of linear search is O(N^2).
#Space complexity of linear search is O(1).
           
#----------Same code -------  
# def linear_search(data,key):
#     index = 0
#     while index < len(data):
#         if data[index] == key:
#             return index
#         index += 1
#     return -1
    
# data = ["prasad", "ginnarapu","varun","kannegari"]
# key = input('Enter Search Item: ')
# res = linear_search(data,key)
# print(key,"occured at:",res,"position")



    