#This assignment showcases list methods

#append
work = ["Plumber", "Bricklayer", "Lawyer"]
work.append("Developer")
print(work)

#clear
work = ["Plumber", "Bricklayer", "Lawyer", "Developer"]
work.clear()
print(work)

#copy
work = ["Plumber", "Bricklayer", "Lawyer", "Developer"]
work.copy()
print(work)

#extend
work = ["Plumber", "Bricklayer", "Lawyer", "Developer"]
food = ["Rice", " Bread", "Buns", "Sweet"]
work.extend(food)
print(work)

#index
food = ["Rice", " Bread", "Buns", "Sweet"]
print(food[3])

#insert
food = ["Rice", " Bread", "Buns", "Sweet"]
food.insert(2, "Mango")
print(food)

food = ["Rice", " Bread", "Buns", "Sweet"]
food.pop(0)
print(food)

#remove
work = ["Plumber", "Bricklayer", "Lawyer", "Developer"]
work.remove("Lawyer")
print(work)

#reverse
work = ["Plumber", "Bricklayer", "Lawyer", "Developer"]
work.sort(reverse=False)
print(work)

#sort
work = ["Plumber", "Bricklayer", "Lawyer", "Developer"]
work.sort()
print(work)
