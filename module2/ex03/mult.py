#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 10:58:56 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 10:58:56 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = first_number * second_number
print("%d x %d = %d" % (first_number, second_number, result))

if result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")



