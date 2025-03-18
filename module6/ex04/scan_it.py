#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 08:11:47 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 08:11:47 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    try:
        print(len(re.findall(sys.argv[1], sys.argv[2])))
    except re.error:
        print("none")
    
