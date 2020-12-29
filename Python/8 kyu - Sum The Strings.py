# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string)
# sum_str("4", "5")    # should output "9"
# sum_str("34", "5")   # should output "39"
# If either input is an empty string, consider it as zero.

# my solution

def sum_str(a, b):
    if a == "":
       a = 0
    if b == "":
       b = 0   
    x = int(a) + int(b)
    return str(x)

# best practiced solution from vote

# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))

