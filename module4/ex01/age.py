#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 11:58:35 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 11:58:35 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    age = int(input("Please tell me your age: "))

    print("You are currently %d years old." % (age))

    years = 10
    while years <= 30:
        print("In %d years, you will be %d years old." % (years, years + age))
        years += 10
except ValueError:
    print("That's not an age. Try again.")
