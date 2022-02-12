class ContactManager():
    
    def __init__(self):
        print("Contact Manager created.")
        self.contacts = {}

    def add_contact(self,name,contact_no):    
        print("Adding contact:" + name + " " + contact_no)
        self.contacts[name] = contact_no
        print("Added contact")
        pass

    def print_contacts(self):
        print("Printing contacts")
        for name, contact_no in self.contacts.items():
            print(name,contact_no)
    
    def search_contacts(self, name):
        print("Searching contacts" + name)
        if name in self.contacts:
            print("Found contact")
        else:
            print("No contact found")

    def remove_contact(self, name):
        print("Removing contact : " + name)
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("No contact found")

    def update_contact(self, name, contact_no):
        if name in self.contacts:
            self.contacts[name] = contact_no
            print("Updating contact : " + name)
        else:
            print("No contact found")
        

    
abd = ContactManager()
print(abd.contacts)
abd.add_contact("Aiman","913467592")
abd.add_contact("Abdullah","9136448012")
abd.print_contacts()
abd.search_contacts("Aiman")
abd.remove_contact("Aiman")
abd.update_contact("Abdullah","9820280449")
abd.print_contacts()