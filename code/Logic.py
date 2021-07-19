""""
== (Equal)
< (Less than)
> (Greater than)
!= (Not equal)
<= (Less or equal than)
>= (Greater or equal than)
"""

pleite = False # bool
if pleite is True:# ==
    print("I have no money!")
else:
    print("I have money!")

bank_account = 1000 # int
if bank_account < 10000:
    print("You have to money!")
else:
    print("Cool for you!")

age = 26
if age < 18:
    print("You are a child!")
elif age < 66: # else if
    print("You are an Erwachsener!")
else:
    print("You are a pensioner")
