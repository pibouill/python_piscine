#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 13:18:19 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 13:18:19 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def array_of_names(names: dict) -> list:
    namebook = []
    for first_name, last_name in names.items():
        namebook.append(first_name.capitalize() + " " + last_name.capitalize())
    return namebook


persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
}

print(array_of_names(persons))
