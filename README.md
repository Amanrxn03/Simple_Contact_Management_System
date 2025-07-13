# Simple_Contact_Management_System

A simple, efficient command-line contact management application built in Python. Store, organize, and manage your contacts with persistent file storage.

## Features

- ✅ **Add Contacts** - Store name, phone number, and email address
- ✅ **View Contacts** - Display all contacts in a formatted list
- ✅ **Search Contacts** - Find contacts by name
- ✅ **Edit Contacts** - Update existing contact information
- ✅ **Delete Contacts** - Remove contacts with confirmation
- ✅ **Persistent Storage** - Contacts saved to JSON file
- ✅ **Input Validation** - Email and phone number validation
- ✅ **Duplicate Prevention** - Prevents duplicate contact names
- ✅ **User-Friendly Interface** - Clean, menu-driven experience

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only built-in Python libraries)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contact-management-system.git
   cd contact-management-system
   ```

2. Run the program:
   ```bash
   python contact_manager.py
   ```

## Usage

### Main Menu
When you run the program, you'll see the main menu:

```
==================================================
           CONTACT MANAGER
==================================================
1. Add Contact
2. View All Contacts
3. Search Contacts
4. Edit Contact
5. Delete Contact
6. Exit
--------------------------------------------------
```

### Adding a Contact
- Choose option 1
- Enter name, phone number, and email
- The program validates input and prevents duplicates
- Contact is automatically saved to `contacts.json`

### Viewing Contacts
- Choose option 2 to see all contacts
- Contacts are displayed in a numbered, formatted list

### Searching Contacts
- Choose option 3
- Enter a name or partial name to search
- Shows all matching contacts

### Editing Contacts
- Choose option 4
- Select a contact by number
- Press Enter to keep current values or type new ones
- Only valid input is accepted

### Deleting Contacts
- Choose option 5
- Select a contact by number
- Confirm deletion when prompted

## File Structure

```
contact-management-system/
├── contact_manager.py      # Main application file
├── contacts.json          # Generated contact storage file
└── README.md             # This file
```

## Data Storage

Contacts are stored in a `contacts.json` file in the same directory as the program. The file is created automatically when you add your first contact.

Example contact data structure:
```json
[
  {
    "name": "John Doe",
    "phone": "+1-555-0123",
    "email": "john.doe@email.com"
  }
]
```

## Input Validation

The program includes robust input validation:

- **Email**: Must follow standard email format (user@domain.com)
- **Phone**: Must contain at least 10 digits (supports various formats)
- **Name**: Cannot be empty and checks for duplicates

## Error Handling

- Graceful handling of file I/O errors
- Input validation with user-friendly error messages
- Keyboard interrupt handling (Ctrl+C)
- JSON parsing error recovery

## Technical Details

- **Language**: Python 3.6+
- **Architecture**: Object-oriented design with Contact and ContactManager classes
- **Storage**: JSON file format for human-readable data
- **Validation**: Regex-based email and phone validation
- **Memory Management**: Efficient loading/saving operations

## Code Structure

### Classes

- `Contact`: Represents individual contact with validation
- `ContactManager`: Handles contact operations and file persistence

### Key Methods

- `add_contact()`: Add new contact with validation
- `view_contacts()`: Display all contacts
- `search_contacts()`: Find contacts by name
- `edit_contact()`: Modify existing contact
- `delete_contact()`: Remove contact with confirmation
- `save_contacts()`: Persist data to JSON file
- `load_contacts()`: Load data from JSON file

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Future Enhancements

- [ ] Export contacts to CSV/Excel
- [ ] Import contacts from file
- [ ] Contact groups/categories
- [ ] Backup and restore functionality
- [ ] GUI interface using tkinter
- [ ] Contact photo support
- [ ] Advanced search filters
- [ ] Sort contacts by different fields


## Author

[Amandeep Pradhan](https://github.com/Amanrxn03)

## Support

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/Amanrxn03/contact-management-system/issues) on GitHub.

---
