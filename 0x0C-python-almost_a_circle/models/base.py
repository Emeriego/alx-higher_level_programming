#!/usr/bin/python3
"""Model creates  base model called Base"""
import csv
import json
import turtle


class Base:
    """This is the base for the other classes in almost a circle project*.
    Attributes:
        __nb_objects (int): The ID or number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Creates new Base object.
        Args:
            id: The id of new object of Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serializes dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """serializes a list of objects to a file.
        """
        f_name = f"{cls.__name__}.json"
        with open(f_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """deserializes a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instantiates a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Returns:
            a list of instantiated classes.
        """
        f_name = str(cls.__name__) + ".json"
        try:
            with open(f_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a csv file.
        """
        f_name = cls.__name__ + ".csv"
        with open(f_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    k_names_list = ["id", "width", "height", "x", "y"]
                else:
                    k_names_list = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, k_names_list=k_names_list)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        """
        f_name = cls.__name__ + ".csv"
        try:
            with open(f_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    k_names_list = ["id", "width", "height", "x", "y"]
                else:
                    k_names_list = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, k_names_list=k_names_list)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using the turtle module.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
