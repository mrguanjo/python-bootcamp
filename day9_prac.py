# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
# "Function": "A piece of code that you can easily call over and over again.",
# "Loop": "The action of doing something over again over again."
# }

# print(programming_dictionary)

# programming_dictionary["Loop"] = "The action of doing something over again over again."


# for key in programming_dictionary:
#     print(key) # key값
# print(programming_dictionary[key]) # value 값

# travel_log = [
#     {
#         "Country": "Germany", 
#         "Cites_visited": ["Berlin", "Hamburg", "Munich"],
#         "total_visits": 12,
#     },
#     {
#         "Country": "France", 
#         "Cities_visited": ["Paris", "Lille", "Dijon"], 
#     }
# ]
# print(travel_log[1]["Country"])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for i in dict:
    dict[i] += 1
    print(dict[i])