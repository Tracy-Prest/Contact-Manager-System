# empty dict to input info
contacts = {}
# mydict = dict(contacts)
index = 0
# menu
def add_contact():
    try:
     name = input("Name:\n")
     phone = int(input("Phone number: \n"))
     email = input("Email: \n").strip()
     k = (name, phone, email)
     contacts[k] = {
               "name": name,
               "phone number": phone,
               "email": email
               } #contacts are values have to create keys for it
    except ValueError:
        print("Please enter alphabets for name, integer for number and any character for email")
    
    print("Contact added")

def view():
    if contacts:
        print("Your contacts: \n")
        # for  k, v in contacts.items():
        for i, (k,v) in enumerate(contacts.items(), start=1):
                print(f"{i}. Name: {v['name']}, Phone: {v['phone number']}, Email: {v['email']}")
                  
            #  if isinstance (k, tuple) and len(k) == 3:
                name, phone, email = k  #unpack k to be viewed in dict
                # for i, contacts in enumerate (contacts, start = 1):

             # print(f"{k}")
            # print(f"Debug - Value stored: {v}")
                # print(f"Name: {name}, Phone: {phone}, Email: {email}")

            # print(f"{k['name']}: {v['name']},{k['phone']}: {v['phone']}, {k['email']}: {v['email']}")
            
        
    else:
        print("no contact available to view")


def search_contact():
    ask = input("Search for contact by name: \n").lower().strip()
    
    found = False #since not found
    for k, v in contacts.items():
            if ask in v['name'].lower():
               found = True #contact found
               print(f"Contact found: Name: {v['name']}, Phone: {v['phone number']}, Email: {v['email']}")
               break
            
    else:
        print("Contact not found") 

    
def delete_contact():
          if contacts:
              
              try:
                      cindex = int(input("Delete a contact by its number: \n"))
                      if 1 <= cindex <= len(contacts):
                          contact_to_delete = list(contacts.items())[cindex - 1 ][0]
                          del contacts[contact_to_delete]
                          print("Contact successfully deleted")
                      else:
                          print("Invalid details")
              except ValueError:
                    print("Enter an integer")
              
          else:
            print("No contact available to delete")
                  
def save_contacts_to_file()  :
    fname = 'contact.txt'
    with open(fname, 'w') as file:
         for (k,v) in contacts.items():
              file.write(f" {v['name']} , {v['phone number']}, {v['email']} \n")
              
         print("Contact saved successfully")

    with open(fname, 'r') as handle:
        content = handle.read()
        print(content)
              


def load_contacts_to_file():
    fname = 'contact.txt'
    content = []
    # for line in contacts.items():
    with open(fname, 'r') as file:
        for line in file:
                content.append(line.strip())
    print("Contacts loaded")
    print("\n".join(content), "\n")
                       
                  

# loop through options
while True:
# options to choose and define functions
    options =  print (""" Choose an option
     1. Add Contact
     2. View Contact
     3. Search for Contact
     4. Delete Contact
     5. Save Contact
     6. Load Contact
                   """)
    choice = input("Enter option between 1-6: \n")

    if choice == "1":
        print("Add a contact")
       
        add_contact()

    elif choice == "2":
         view()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        # delete = input("Do you want to delete a contact? \n (yes or no)\n").lower()
        # for k,v in contacts.items():
        #     if delete == "yes":
                view()

                delete_contact()

    elif choice == "5":
       save_contacts_to_file()

    elif choice == "6":
        load_contacts_to_file()


        


