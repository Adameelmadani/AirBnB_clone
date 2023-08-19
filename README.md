# AirBnB Clone Console

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/2560px-Airbnb_Logo_B%C3%A9lo.svg.png" width="400">

## Description

This is a console application for the AirBnB clone project. The console allows users to interact with various classes and perform CRUD (Create, Read, Update, Delete) operations on instances of these classes. It provides a command-line interface to manage State, City, Amenity, Place, and Review objects.

The project is part of the larger AirBnB clone project, which aims to replicate the functionality of the popular vacation rental platform AirBnB. The console serves as a tool for managing and manipulating data related to different entities in the AirBnB system.

## Features

- Create new instances of State, City, Amenity, Place, and Review classes.
- Retrieve instances based on their ID and class name.
- Update attributes of instances.
- Delete instances.
- Display all instances of a class.
- Count the number of instances of a class.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/AirBnB_clone.git
```

2. Navigate to the project directory:

```bash
cd AirBnB_clone
```

3. Run the console:

```bash
./console.py
```

## Usage

The console provides a command-line interface where you can enter various commands to interact with the AirBnB objects. Available commands include:

- create: Create a new instance of a class.
- show: Display details of a specific instance.
- destroy: Delete an instance based on its ID.
- update: Update the attributes of an instance.
- all: Display all instances of a class.
- count: Get the count of instances of a class.
  For detailed usage instructions, use the help command within the console.

### Examples

Creating a new State instance:

```bash
(hbnb) create State name="California"
```

Showing details of a City instance:

```bash
(hbnb) show City 12345-6789
```

Updating attributes of a Place instance:

```bash
(hbnb) update Place 9876-5432 number_rooms 3
```

Testing

To run unittests for the console, use the following command:

```bash
python -m unittest discover tests
```

Make sure to write comprehensive tests to cover all functionalities of the console.

## AUTHORS

- Yonatan Addis <yonatanaddis0257@gmail.com>
- Adam El Madani <adamelmadani0129@gmail.com>
