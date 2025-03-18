#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 14:03:40 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 14:03:40 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def famous_births(names: dict[str, dict[str, str]]) -> None:
    try:
        res = []
        for f_name in names.values():
            if "date_of_birth" in f_name and "name" in f_name:
                res.append((f_name["date_of_birth"], f_name["name"]))
        res = sorted(res)
        for date, name in res:
            print(f"{name} is a great scientist born in {date}.")
    except KeyError as e:
        print(f"Error: Missing required field - {e}")
    except Exception as e:
        print(f"Error: {str(e)}")


# your method definition here
women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
        "bibou": {"name": "Bibou Doe", "date_of_birth": "2100"},
        "cleo": {"name": "Cleopatra VII Thea Philopator", "date_of_birth": "-2024"},
        "who": {"name"},
}
famous_births(women_scientists)
