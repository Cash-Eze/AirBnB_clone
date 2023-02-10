#!/usr/bin/python3
"""My console class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ my HBNB command console"""
    prompt = '(hbnb)'
    file = None

    def do_EOF(self, args):
	"""define EOF command- quit program"""
        return True

    def do_quit(self, args):
	"""define quit command- quit program"""
	return True

    def emptyline(self):
        """emptyline shouldn't exexute anything"""
	return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand.().cmdloop()
