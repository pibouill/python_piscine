#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 13:07:02 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 13:07:02 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    first_number = int(input("Give me the first number: "))
    second_number = int(input("Give me the second number: "))

    print("Thank you!")
    if second_number != 0:
         print("%d - %d = %d" % (first_number, second_number, first_number - second_number))
         print("%d / %d = %d" % (first_number, second_number, first_number / second_number))
         print("%d + %d = %d" % (first_number, second_number, first_number + second_number))
         print("%d * %d = %d" % (first_number, second_number, first_number * second_number))
    else:
        print("not possible")
        quit()
except ValueError:
    print("I said, a number.")
