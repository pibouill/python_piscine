#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 16:08:30 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 16:08:30 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

age = int(input("Please tell me your age: "))

print("You are currently", age, "years old.")

years = 10

while years <= 30:
	print("In", years, "years, you'll be", age + years, "years old.")
	years += 10
