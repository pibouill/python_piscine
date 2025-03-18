#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 11:01:44 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 11:01:44 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def greetings(name=None):  # None handles cases without args
    if name is None:
        print("Hello, noble stranger.")
    elif isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
