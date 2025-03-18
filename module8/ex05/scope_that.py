#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 11:37:44 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 11:37:44 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def add_one(num):
    num = num + 1


n = 42
print(n)
add_one(n)  # integers are immutable so n remains unchanged
# n = add_one(n) would add one to n
print(n)
