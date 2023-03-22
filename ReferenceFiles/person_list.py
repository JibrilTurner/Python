class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is %s" % self.name)

people = []

while True:
    choice = input("Enter 'a' to add a person, 'p' to print the list, or 'q' to quit, or press z to increment by one : ")
    if choice == 'q':
        break
    elif choice == 'a':
        name = int(input("Enter person's name: "))
        person = Person(name)
        people.append(person)
        print("Person added.")
    elif choice == 'p':
        print("List of people:")
        for person in people:
            person.introduce()
    elif choice == 'z':
        for person in people:
            person.name += 1
        print("Values incremented by one.")
    else:
        print("Invalid choice. Please try again.")
