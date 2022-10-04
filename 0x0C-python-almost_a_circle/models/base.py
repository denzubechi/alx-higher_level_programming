#!/usr/bin/python3
"""
a module for base class
"""

import json
import csv
import turtle


class Base:
    """
    Defining a base class module
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        a constructor function
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list of dictionaries to json string
        :param list_dictionaries: list of dictionaries
        :return: json string
        """
        if (list_dictionaries is None or list_dictionaries == []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save list of objects to file
        :param list_objs: list of objects
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            if (list_objs is None or len(list_objs) == 0):
                file.write("[]")
            else:
                list_dict = [list.to_dictionary() for list in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        load list of objects from json string
        :param json_string: json string
        :return: JSON string representation of list of objects
        """
        if (json_string is None or json_string == "[]"):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create new list of objects
        :param dictionary: dict object
        :return: list of objects
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_values = cls(1, 1)
            else:
                new_values = cls(1)
            new_values.update(**dictionary)
            return new_values

    @classmethod
    def load_from_file(cls):
        """
        load list of objects from file
        :return: list of objects
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save list of objects to csv file
        :param list_objs: list of objects
        :return:
        """
        filename = str(cls.__name__) + ".csv"

        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        load list of objects from csv file
        :return:
        """
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw list of rectangles and list of squares
        :param list_rectangles: list of rectangles
        :param list_squares: list of squares
        """
        turt_tle = turtle.Turtle()
        turt_tle.screen.bgcolor("#b7312c")
        turt_tle.pensize(3)
        turt_tle.shape("turtle")

        turt_tle.color("#ffffff")
        for rect in list_rectangles:
            turt_tle.showturtle()
            turt_tle.up()
            turt_tle.goto(rect.x, rect.y)
            turt_tle.down()
            for i in range(2):
                turt_tle.forward(rect.width)
                turt_tle.left(90)
                turt_tle.forward(rect.height)
                turt_tle.left(90)
            turt_tle.hideturtle()

        turt_tle.color("#b5e3d8")
        for sq in list_squares:
            turt_tle.showturtle()
            turt_tle.up()
            turt_tle.goto(sq.x, sq.y)
            turt_tle.down()
            for i in range(2):
                turt_tle.forward(sq.width)
                turt_tle.left(90)
                turt_tle.forward(sq.height)
                turt_tle.left(90)
            turt_tle.hideturtle()

        turtle.exitonclick()
