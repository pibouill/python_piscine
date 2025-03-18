#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 08:21:17 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 08:21:17 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
    print("none")
else:
    try:
        param = input("What was the parameter? ")
        if param == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")
    except EOFError:
        sys.exit("\nClosing")
    except KeyboardInterrupt:
        sys.exit("\nctrl c")
