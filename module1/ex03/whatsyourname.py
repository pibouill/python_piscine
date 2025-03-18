#!/bin/bash
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 10:21:07 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 10:21:07 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first_name = input("Hey, what's your first name? : ")
last_name = input("And your last name? : ")

print("Well, pleased to meet you, %s %s." % (first_name.strip(), last_name.strip()))
