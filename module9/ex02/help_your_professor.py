#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 13:55:53 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 13:55:53 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def average(students: dict) -> int:
    grades = 0
    for grade in students.values():
        try:
            if grade < 0:
                print("Wrong grade")
                quit()
            grades += grade
        except ValueError:
            print("ValueError")
            quit()
        except TypeError:
            print("Wrong Type in dic")
            quit()
    return grades / len(students)


class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9,
        # "caro": -42
}

class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
