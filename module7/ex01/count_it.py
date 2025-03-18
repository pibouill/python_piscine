#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 08:25:40 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 08:25:40 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print("none")
else:
    print("parameters: %d" % (len(sys.argv) - 1))
    for arg in sys.argv[1:]:
        print("%s: %d" % (arg, len(arg)))
        # this is apparently old formatting style
        # should do instead
        # print(f"{arg}: {len(arg)}")
