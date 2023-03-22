class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is %s" % name)

people = []

while True:
    choice = input("Enter 'a' to add a person, 'p' to print the list, or 'q' to quit: ")
    if choice == 'q':
        break
    elif choice == 'a':
        name = input("Enter person's name: ")
        person = Person(name)
        people.append(person)
        print("Person added.")
    elif choice == 'p':
        print("List of people:")
        for person in people:
            person.introduce()
    else:
        print("Invalid choice. Please try again.")
