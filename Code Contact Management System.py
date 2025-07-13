import json
import os
import re
from typing import Dict, List, Optional

class Contact:
    """Represents a single contact with name, phone, and email."""
    
    def __init__(self, name: str, phone: str, email: str):
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()
    
    def to_dict(self) -> Dict[str, str]:
        """Convert contact to dictionary for JSON serialization."""
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Contact':
        """Create contact from dictionary."""
        return cls(data['name'], data['phone'], data['email'])
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

class ContactManager:
    """Manages a collection of contacts with file persistence."""
    
    def __init__(self, filename: str = "contacts.json"):
        self.filename = filename
        self.contacts: List[Contact] = []
        self.load_contacts()
    
    def load_contacts(self) -> None:
        """Load contacts from file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.contacts = [Contact.from_dict(contact_data) for contact_data in data]
                print(f"Loaded {len(self.contacts)} contacts from {self.filename}")
            except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
                print(f"Error loading contacts: {e}")
                self.contacts = []
        else:
            print(f"No existing contact file found. Starting with empty contact list.")
    
    def save_contacts(self) -> None:
        """Save contacts to file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump([contact.to_dict() for contact in self.contacts], f, indent=2)
            print(f"Contacts saved to {self.filename}")
        except Exception as e:
            print(f"Error saving contacts: {e}")
    
    def validate_email(self, email: str) -> bool:
        """Basic email validation."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone: str) -> bool:
        """Basic phone validation - allows digits, spaces, dashes, parentheses."""
        pattern = r'^[\d\s\-\(\)\+]+$'
        return re.match(pattern, phone) is not None and len(phone.strip()) >= 10
    
    def add_contact(self) -> None:
        """Add a new contact with user input validation."""
        print("\n--- Add New Contact ---")
        
        # Get and validate name
        while True:
            name = input("Enter name: ").strip()
            if name:
                # Check for duplicate names
                if any(contact.name.lower() == name.lower() for contact in self.contacts):
                    overwrite = input(f"Contact '{name}' already exists. Overwrite? (y/n): ").lower()
                    if overwrite == 'y':
                        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
                        break
                    else:
                        continue
                else:
                    break
            else:
                print("Name cannot be empty. Please try again.")
        
        # Get and validate phone
        while True:
            phone = input("Enter phone number: ").strip()
            if phone and self.validate_phone(phone):
                break
            else:
                print("Invalid phone number. Please enter at least 10 digits.")
        
        # Get and validate email
        while True:
            email = input("Enter email address: ").strip()
            if email and self.validate_email(email):
                break
            else:
                print("Invalid email format. Please try again.")
        
        # Create and add contact
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"\nContact '{name}' added successfully!")
        self.save_contacts()
    
    def view_contacts(self) -> None:
        """Display all contacts."""
        if not self.contacts:
            print("\nNo contacts found.")
            return
        
        print(f"\n--- Contact List ({len(self.contacts)} contacts) ---")
        for i, contact in enumerate(self.contacts, 1):
            print(f"\n{i}. {contact}")
            print("-" * 40)
    
    def search_contacts(self) -> Optional[List[Contact]]:
        """Search contacts by name."""
        if not self.contacts:
            print("\nNo contacts to search.")
            return None
        
        search_term = input("Enter name to search: ").strip().lower()
        if not search_term:
            return None
        
        matches = [c for c in self.contacts if search_term in c.name.lower()]
        
        if matches:
            print(f"\n--- Search Results ({len(matches)} found) ---")
            for i, contact in enumerate(matches, 1):
                print(f"{i}. {contact}")
                print("-" * 40)
            return matches
        else:
            print("No contacts found matching your search.")
            return None
    
    def edit_contact(self) -> None:
        """Edit an existing contact."""
        if not self.contacts:
            print("\nNo contacts to edit.")
            return
        
        # Show contacts and get selection
        self.view_contacts()
        
        try:
            choice = int(input(f"\nEnter contact number to edit (1-{len(self.contacts)}): "))
            if 1 <= choice <= len(self.contacts):
                contact_to_edit = self.contacts[choice - 1]
                print(f"\nEditing contact: {contact_to_edit.name}")
                
                # Edit each field
                print("\nPress Enter to keep current value:")
                
                new_name = input(f"Name ({contact_to_edit.name}): ").strip()
                if new_name:
                    contact_to_edit.name = new_name
                
                new_phone = input(f"Phone ({contact_to_edit.phone}): ").strip()
                if new_phone:
                    if self.validate_phone(new_phone):
                        contact_to_edit.phone = new_phone
                    else:
                        print("Invalid phone number. Keeping original.")
                
                new_email = input(f"Email ({contact_to_edit.email}): ").strip()
                if new_email:
                    if self.validate_email(new_email):
                        contact_to_edit.email = new_email
                    else:
                        print("Invalid email format. Keeping original.")
                
                print("Contact updated successfully!")
                self.save_contacts()
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def delete_contact(self) -> None:
        """Delete a contact."""
        if not self.contacts:
            print("\nNo contacts to delete.")
            return
        
        # Show contacts and get selection
        self.view_contacts()
        
        try:
            choice = int(input(f"\nEnter contact number to delete (1-{len(self.contacts)}): "))
            if 1 <= choice <= len(self.contacts):
                contact_to_delete = self.contacts[choice - 1]
                confirm = input(f"Are you sure you want to delete '{contact_to_delete.name}'? (y/n): ").lower()
                
                if confirm == 'y':
                    self.contacts.pop(choice - 1)
                    print(f"Contact '{contact_to_delete.name}' deleted successfully!")
                    self.save_contacts()
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main program loop."""
    manager = ContactManager()
    
    while True:
        print("\n" + "="*50)
        print("           CONTACT MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("-"*50)
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                manager.add_contact()
            elif choice == '2':
                manager.view_contacts()
            elif choice == '3':
                manager.search_contacts()
            elif choice == '4':
                manager.edit_contact()
            elif choice == '5':
                manager.delete_contact()
            elif choice == '6':
                print("\nThank you for using Contact Manager!")
                break
            else:
                print("Invalid choice. Please enter 1-6.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
