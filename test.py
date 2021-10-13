def times_table():
    table_number = 0
    while table_number < 1 or table_number >12:
        table_number = int(input("Which multiplication table would you like to view? : "))
    for i in range(1,13):
        product = i*table_number
        print(f"{table_number} x {i} = {product}")

"""
Excellent code Luka. I like the while loop that checks the user input. Could you make the code go back to the start 
once it's finished so the user can view another table?
"""
tab = 1
while tab ==1:
    times_table()