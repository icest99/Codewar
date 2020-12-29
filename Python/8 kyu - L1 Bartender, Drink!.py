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

