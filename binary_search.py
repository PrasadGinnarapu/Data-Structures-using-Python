# def test_location(query,cards, mid):
#     if cards[mid] == query:
#         if mid-1 >= 0 and cards[mid-1] == query:
#             return 'left'
#         else:
#             return 'found'
#     elif cards[mid] < query:
#         return 'left'
#     else:
#         return 'right'
    
# def locate_card(query,cards):
#     low, high = 0, len(cards)-1
#     while low <= high:   
#         mid = (low + high)//2
#         result = test_location(query,cards,mid)     
#         if result == 'found':
#             return mid
#         elif result == 'left':
#             high = mid - 1
#         elif result == 'right':
#             low = mid + 1
#     return -1

# cards = ["p","a","a","s","a"]
# query = input('Enter Query: ')
# print(locate_card(query,cards))


# Note: 
#     Time complexity of Binary Search O(log N)
#     Space complexity of Binary Search O(1)
