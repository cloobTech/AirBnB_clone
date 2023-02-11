This is a project on the implementation of the back-end console of the airbnb clone.

Classes:
AirBnB Clone utilizes the following classes:

BaseModel
FileStorage
User
State
City
Amenity
Place
Review

PUBLIC INSTANCE ATTRIBUTES
id
created_at
updated_at

PUBLIC INSTANCE METHODS
save
to_dict	all
new
save
reload

PUBLIC CLASS ATTRIBUTES
email
password
first_name
last_name
name
state_id
city_id
user_id
description
number_of_rooms
number_of_bathrooms
max_guest
price_by_night
latitude
longitude
amenity_ids
place_id
user_id
text

PRIVATE CLASS ATTRIBUTES
file_path
objects
						
Storage:
The above classes are handled by the abstracted storage engine defined in the FileStorage class.

Every time the backend is initialized, AirBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

Console:
The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

Using the Console
The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
Alternatively, to use the AirBnB console in interactive mode, run the file console.py by itself:

$ ./console.py
While running in interactive mode, the console displays a prompt for input:

$ ./console.py
(hbnb) 
To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

$ ./console.py
(hbnb) quit
$
$ ./console.py
(hbnb) EOF
$
Console Commands
The AirBnb=B console supports the following commands:

	*create
Usage: create <class>
Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

	*show
Usage: show <class> <id> or <class>.show(<id>)
Prints the string representation of a class instance based on a given id.
 
	*destroy
Usage: destroy <class> <id> or <class>.destroy(<id>)
Deletes a class instance based on a given id. The storage file file.json is updated accordingly.

	*all
Usage: all or all <class> or <class>.all()
Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.
 
	*count
Usage: count <class> or <class>.count()
Retrieves the number of instances of a given class.
 
	*update
Usage: update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>).
Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.

	*Testing 📏
Unittests for the AirBnb project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

$ python3 unittest -m discover tests
Alternatively, you can specify a single test file to run at a time:

$ python3 unittest -m tests/test_console.py
