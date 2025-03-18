#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 13:34:45 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 13:34:45 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def find_the_redheads(dic: dict):
    rdh = []
    for name, color in dic.items():
        if color == "red":
            rdh.append(name)
    return rdh


dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
}

print(find_the_redheads(dupont_family))
