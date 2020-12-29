word_list = {
    "Jabroni":"Patron Tequila",
    "School Counselor":"Anything with Alcohol",
    "Programmer":"Hipster Craft Beer",
    "Bike Gang Member":"Moonshine",
    "Politician":"Your tax dollars",
    "Rapper":"Cristal"
    
}

def get_drink_by_profession(param):
    param_valid = param.title()
    if param_valid in word_list:
        return(word_list[param_valid])
    else:
        return "Beer"

# Best Practiced Solution by vote
# d = {
#     "jabroni": "Patron Tequila",
#     "school counselor": "Anything with Alcohol",
#     "programmer": "Hipster Craft Beer",
#     "bike gang member": "Moonshine",
#     "politician": "Your tax dollars",
#     "rapper": "Cristal"
# }

# def get_drink_by_profession(s):
#     return d.get(s.lower(), "Beer")

#he changed the key to lowercases to make it easier