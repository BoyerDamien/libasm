# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/20 09:03:17 by dboyer            #+#    #+#              #
#    Updated: 2020/05/24 11:37:45 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME    			=	libasm.a

SRCS    			=	srcs/ft_read.s\
						srcs/ft_write.s\
						srcs/ft_strlen.s\
						srcs/ft_strcpy.s\
						srcs/ft_strcmp.s\
						srcs/ft_strdup.s

MAIN 				= 	srcs/main.c

OBJS    			= 	$(SRCS:.s=.o)
MAIN_OBJS    		= 	$(MAIN:.c=.o)

NASM				=	nasm -f elf64
CC      			= 	clang

RM      			= 	rm -f

HEADERS 			= 	-I ./includes/

CFLAGS  			= 	-Werror -Wall -Wextra -Ofast -pedantic-errors ${HEADERS}

INCS				=	./includes/libasm.h

################################################################################
#									cube3d make
################################################################################

%.o: %.s
	$(NASM) $< -o $@

%.o: %.c $(INCS)
	$(CC) $(CFLAGS) -c $< -o $@

all     :	$(NAME)

$(NAME) :	$(OBJS)
		ar rc $(NAME) $(OBJS)

clean   :
	$(RM) $(OBJS)
	$(RM) ${MAIN_OBJS}
	$(RM) a.out

fclean  : clean
	$(RM) $(NAME)

test    : $(NAME) $(MAIN_OBJS)
	$(CC) $(CFLAGS) $(NAME) $(OBJS) $(MAIN_OBJS)

re      : fclean all

################################################################################
#												Extra make
################################################################################

norm: fclean
	~/.norminette/norminette.rb

.PHONY  :	all clean fclean re%
