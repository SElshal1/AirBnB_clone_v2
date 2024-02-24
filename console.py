#!/usr/bin/python3
"""Module for console"""
import sys
import cmd
from models.base_model import BaseModel
from models.place import Place
from models.__init__ import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City

class HBNBCommand(cmd.Cmd):
    """HBNB console functionality"""

    # Prompt for interactive/non-interactive modes determind
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """ON isatty is false printd"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Command line reformated for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # General formating scan- i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # Line left to right parse
            pln = line[:]  # Line parsed

            # isolate <class name>
            _cls = pln[:pln.find('.')]

            # isolate and validate <command>
            _cmd = pln[pln.find('.') + 1:pln.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pln = pln[pln.find('(') + 1:pln.find(')')]
            if pln:
                # partition args: (<id>, [<delim>], [<*args>])
                pln = pln.partition(', ')  # Convert pln to tuple

                # isolate _id, stripping quotes
                _id = pln[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pln = pln[2].strip()  # pln is now str
                if pln:
                    # check for *args or **kwargs
                    if pln[0] == '{' and pln[-1] == '}'\
                            and type(eval(pln)) is dict:
                        _args = pln
                    else:
                        _args = plin.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, l):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """HBNB console exit method"""
        exit()

    def help_quit(self):
        """ Help documentation for quit printd  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ EOF to exit program handled"""
        print()
        exit()

    def help_EOF(self):
        """ Help documentation for EOF printd"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Emptyline method of CMD override"""
        pass

    def do_create(self, args):
        """ Object of any class created"""
        try:
            if not args:
                raise SyntaxError()
            arglist = args.split(" ")
            kw = {}
            for arg in argList[1:]:
                argSplited = arg.split("=")
                argSplited[1] = eval(argSplited[1])
                if type(argSplited[1]) is str:
                    argSplited[1] = argSplited[1].replace("_", " ").replace('"', '\\"')
                kw[argSplited[0]] = argSplited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        newInstance = HBNBCommand.classes[arglist[0]](**kw)
        newInstance.save()
        print(newInstance.id)

    def help_create(self):
        """ Help info for create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method shows an individual object """
        n = args.partition(" ")
        c_name = n[0]
        c_id = n[2]

        # guards against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if not c_id:
            print("** instance id missing **")
            return


        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help info for show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Specified object destroyed"""
        n = args.partition(" ")
        c_name = n[0]
        c_id = n[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_name:
            print("** class name missing **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        k = c_name + "." + c_id

        try:
            del(storage.all()[k])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help info for destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ All objects shown else all objects of a class"""
        printList = []

        if args:
            args = args.split(' ')[0]  # Possible trailing args removed
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for a, b in storage.all(HBNBCommand.classes[args]).items():
                printList.append(str(b))
        else:
            for a, b in storage.all().items():
                printList.append(str(b))
        print(printList)

    def help_all(self):
        """Help info for all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Current no. of class instances countd"""
        c = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                c += 1
        print(c)

    def help_count(self):
        """help info for do count"""
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Certain object updated with new info """
        cName = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            cName = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if cName not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for k, att_name in enumerate(args):
            # block only runs on even iterations
            if (k % 2 == 0):
                att_val = args[k + 1]  # Item followin is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # Updates savd to file

    def help_update(self):
        """ Help info for update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
