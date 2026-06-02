# Activity - Search And Add Contacts

## Goal

Practice lists, keys, controlled inputs, and forms.

## Task 1: Search Contacts

Add a search input to the contact list.

Requirements:

- input is controlled by state
- filter contacts by name or email
- show empty state if no contacts match

Flow:

```text
User types
-> search state changes
-> filtered list is calculated
-> UI re-renders
```

## Task 2: Add Contact Form

Add a form with:

- name
- email
- status

Requirements:

- controlled inputs
- `onSubmit`
- `event.preventDefault()`
- validation for empty name/email
- add new contact to list
- clear form after submit

## Demo Questions

```text
Where is the search value stored?
How do you render the contact list?
What key did you use?
How does a new contact get added to the UI?
```

