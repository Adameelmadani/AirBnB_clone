#!/usr/bin/python3
"""
This is console module
"""
import cmd
from models.base_model import BaseModel
from models.user import User

from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import models

"""
This is command line module
BaseModel class from models/base_model
"""


class HBNBCommand(cmd.Cmd):
    """
    Our HBNB command class
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        help quit command
        """
        print("quit:\nExit the program")

    def do_EOF(self, line):
        """
        End of file command to exit the program
        """
        print()
        return True

    def help_EOF(self):
        """
        help EOF command
        """
        print("EOF:\nExit the program - press Ctr-D or enter EOF")

    def emptyline(self):
        """
        An empty line passed to the console
        """
        pass

    def do_create(self, line):
        """
        create command:
            Creates a new instance of BaseModel, saves it and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            new_obj = HBNBCommand.classes[line]()
            new_obj.save()
            print(new_obj.id)

    def help_create(self):
        """
        help for create command
        """
        print("create:\nCreate an instance")

    def do_show(self, line):
        """
        show command:
            Prints the string representation of an instance.
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                name = args[0] + "." + args[1]
                if name not in models.storage.all().keys():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[name])

    def help_show(self):
        """
        help for show command
        """
        print("show:\nShow the string representation of an instance")

    def do_destroy(self, line):
        """
        destroy command:
            Deletes an instance based on the class name and id.
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                name = args[0] + "." + args[1]
                if name not in models.storage.all().keys():
                    print("** no instance found **")
                else:
                    del models.storage.all()[name]
                    models.storage.save()

    def help_destroy(self):
        """
        help for destroy command
        """
        print("destroy:\nDestroy an instance based on the class name and id")

    def do_all(self, line):
        """
        all command:
            Prints all string representation of all instances.
        """
        list_str = []
        if line:
            if line not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for key, value in models.storage.all().items():
                    if line in key:
                        list_str.append(str(value))
                print(list_str)
        else:
            for value in models.storage.all().values():
                list_str.append(str(value))
            print(list_str)
        list_str.clear()

    def help_all(self):
        """
        help for all command
        """
        print("all:\nShows a list of string representations")

    def do_update(self, line):
        """
        update command:
            Updates an instance by adding or updating attribute.
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                name = args[0] + "." + args[1]
                if name not in models.storage.all().keys():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    value = eval(args[3])
                    try:
                        value = int(args[3])
                        a = True
                    except ValueError:
                        a = False
                    if a is False:
                        try:
                            value = float(args[3])
                        except ValueError:
                            pass
                    obj = models.storage.all()[name]
                    setattr(obj, args[2], value)
                    obj.save()

    def help_update(self):
        """
        help for update command
        """
        print("help:\nCreate or Update an attribute")

    def default(self, line):
        """
        default function
        """
        args = line.split(".")
        if len(args) == 2:
            if args[1] == "all()":
                self.onecmd("all " + args[0])
            elif args[1] == "count()":
                count = 0
                objs = models.storage.all()
                for k in objs.keys():
                    if args[0] in k:
                        count += 1
                print(count)
            elif args[1].startswith("show"):
                show_id = ""
                args[1] = args[1][4:]
                for i in args[1]:
                    if i != "(" and i != ")" and i != "\"":
                        show_id += i
                self.onecmd("show " + args[0] + " " + show_id)
            elif args[1].startswith("destroy"):
                show_id = ""
                args[1] = args[1][7:]
                for i in args[1]:
                    if i != "(" and i != ")" and i != "\"":
                        show_id += i
                self.onecmd("destroy " + args[0] + " " + show_id)
            elif args[1].startswith("update"):
                elems = args[1].split(", ")
                update_id = ""
                elems[0] = elems[0][6:]
                for i in elems[0]:
                    if i != "(" and i != "\"":
                        update_id += i
                if "{" not in args[1]:
                    if elems[1][0] == "\"" and elems[1][-1] == "\"":
                        elems[1] = elems[1][1:-1]
                    elems[2] = elems[2][0:-1]
                    s = args[0] + " " + update_id + " " + elems[1] + " "
                    self.onecmd("update " + s + elems[2])
                else:
                    elems = args[1].split(", ", 1)
                    elems[0] = elems[0][6:]
                    s = "update " + args[0] + " " + update_id + " "
                    elems[1] = elems[1][1:-2]
                    update_dict = elems[1].split(", ")
                    for elem_dict in update_dict:
                        att = elem_dict.split(": ")
                        if att[0][0] == "\"" or att[0][0] == "\'":
                            att[0] = att[0][1:-1]
                        self.onecmd(s + att[0] + " " + att[1])
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
