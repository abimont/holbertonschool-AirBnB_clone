# AirBnB clone - The console
<p align="center"> <img src="https://cdn.pixabay.com/photo/2013/07/13/13/41/bash-161382__340.png"/> </p>

### Command interpreter to manage the AirBnB clone objects.

The console is part of the AirBnB project in the Fundations Program at Holberton School. This will be the first to step to build the entire application and we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later.

This abstraction will also allow us to change the type of storage easily without updating all of our codebase. The console will be a tool to validate this storage engine.

![Flowchart](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221028T214029Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bd8ee4dbcb71f74bd66d5d9d60774b97cec0a90baa27b9e3f2ca085fd7467e50)

The command interpreter will be developed in the following way:

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine.

## Usage
This command interpreter should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Concepts to be considered.

- Python packages
- Serialization/Deserialization
- *args, **kwargs
- datetime
- Unittest
- UUID
- cmd


## Contributors
Abigail Montes - GitHub: [abimont](https://github.com/abimont)

Miguel Torres - GitHub: [MiguelGit20](https://github.com/MiguelGit20)
