#!/usr/bin/python3
"""program called console.py that contains the entry point of the command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class cmd
    """
    prompt = "(hbnb) "
    val_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.val_classes:
            print("** class doesn't exist **")
        else:
            instance1 = BaseModel()
            instance1.save()
            print(instance1.id)
        def do_show(self, arg):
            command = shlex.split(arg)
            if len(command) == 0:
                print("** class name missing **")
            elif command[0] not in self.val_classes:
                print("** class doesn't exist **")
            elif len(command) < 2:
                print("** instance id missing **")
            else:
                obje = storage.all()
                key = f"{commad[0]}.{commad[1]}"
                if key in obje:
                    print(obje[key])
                else:
                    print("** no instance found **")
        def do_destroy(self, arg):
            command = shlex.split(arg)
            if len(command) == 0:
                print("** class name missing **")
            elif command[0] not in self.val_classes:
                print("** class doesn't exist **")
            elif len(command) < 2:
                print("** instance id missing **")
            else:
                obje = storage.all()
                key = f"{commad[0]}.{commad[1]}"
                if key in obje:
                    del obje[key]
                    storage.save()
                else:
                    print("** no instance found **")


    def do_EOF(self, arg):
        """Handle the end of file input"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
