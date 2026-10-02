print("Hello world!\nThis text is for my practice so I will try")
print("Enter some number. I will try to letter your text:")
a = input()
while not a.isdigit():
    print("So please write numder!")
    a = input()
for x in str(a):
    print(x)
print("Wow, this numder is great! \nWhat do you think about my code? :)")
input("Thats all")
