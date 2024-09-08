# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 11:28:53 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 11:45:41 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# strip ?

first_name = input("Hey, what's your first name? : ")

last_name = input("And your last name? : ")

whole_name = "%s %s" % (first_name, last_name)
print("Well, pleased to meet you,", whole_name + ".")
