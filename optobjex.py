class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    def __repr__(self):
        return '%s: %s | %s' % (self.name, self.email, self.phone)
    def greet(self, other_person):
        print ("Howdy, %s! I'm %s!" % (other_person.name, self.name))
        self.greeting_count += 1
    def print_contact_info(self):
        print (self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    def add_friend(self, other_person):
        self.friends.append(other_person)
    def num_friends(self):
        print (len(self.friends))

sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
jordan = Person("Jordan","jordan@aol.com","495-586-3456")
dee_dee = Person("Dee Dee","deedee@gmail.com","483-210-8201")

sonny.greet(jordan)
jordan.greet(sonny)

print (sonny.email + "\n" + sonny.phone)
print (jordan.email + "\n" + jordan.phone)

class Vehicle(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print (str(self.year) + " " +  self.make + " " + self.model)

car = Vehicle("Nissan","Leaf",2015)
car.print_info()

sonny.print_contact_info()

jordan.add_friend(sonny)
sonny.add_friend(jordan)
jordan.num_friends()

print (sonny.greeting_count)
print (jordan.__repr__()) # You need to call __repr__() as a method for it to render as the literal string you want it to.

sonny.greet(dee_dee)