#!/usr/bin/python3
"""
Module ``console``
Class HBNBCommand that creates the console.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Clean way to exit
        """
        return True

    def emptyline(self):
        """Empty line doesn't execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
