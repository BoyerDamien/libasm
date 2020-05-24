#include "libasm.h"

int	test_strlen(int argc, char *argv[])
{
	if (argc <= 2)
	{
		printf(ERROR_NEED_ARG);
		return (EXIT_SUCCESS);
	}
	printf("ft_strlen\t%lu\nstrlen\t\t%lu\n", ft_strlen(argv[2]), strlen(argv[2]));
	return (EXIT_SUCCESS);
}

int	test_strcpy(int argc, char *argv[])
{
	char	*str1 = strdup(argv[2]);
	char	*str2 = strdup(argv[2]);

	if (argc <= 3)
	{
		printf(ERROR_NEED_ARG);
		return (EXIT_SUCCESS);
	}
	printf("strcpy\t\t|%s|\nft_strcpy\t|%s|\n", strcpy(str1, argv[3]), ft_strcpy(str2,argv[3]));
	if (strlen(argv[3]) != 0)
		argv[3][0] = '_';
	printf("str1 : %s\n", str1);
	printf("str2 : %s\n", str2);
	free(str1);
	free(str2);
	return (EXIT_SUCCESS);
}

int	test_strcmp(int argc, char *argv[])
{
	if (argc <= 3)
	{
		printf(ERROR_NEED_ARG);
		return (EXIT_SUCCESS);
	}
	printf("ft_strcmp\t|%d|\nstrcmp\t\t|%d|\n", ft_strcmp(argv[2], argv[3]), strcmp(argv[2],argv[3]));
	return (EXIT_SUCCESS);
}

int test_write(int argc, char *argv[])
{
	int fd;

	if (argc <= 4)
	{
		printf(ERROR_NEED_ARG);
		return (EXIT_SUCCESS);
	}
	if ((fd = atoi(argv[2])) == 3)
		fd = open("test_write.txt", O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
	printf("write\t : ");
	fflush(stdout);
	int ret_o = write(fd, argv[3], atoi(argv[4]));
	printf("\t| ret = %d\nft_write : ", ret_o);
	fflush(stdout);
	int ret_m = ft_write(fd, argv[3], atoi(argv[4]));
	printf("\t| ret = %d\n", ret_m);
	close(fd);
	return (EXIT_SUCCESS);
}

int test_read(int argc, char *argv[])
{
	int fd1;
	int	fd2;
	char *str1;
	char *str2;

	if (argc <= 4)
	{
		printf(ERROR_NEED_ARG);
		return (EXIT_SUCCESS);
	}
	if ((fd1 = atoi(argv[2])) == 3 || (fd2 = atoi(argv[2])) == 3)
	{
		fd1 = open("test_read.txt", O_RDONLY);
		fd2 = open("test_read.txt", O_RDONLY);
	}
	else if (atoi(argv[2]) == 4)
	{
		fd1 = open("test_read.txt", O_WRONLY);
		fd2 = open("test_read.txt", O_WRONLY);
	}
	str1 = strdup(argv[3]);
	str2 = strdup(argv[3]);
	printf("read\t : %s\t| ret = %zd\n", str1, read(fd1, str1, atoi(argv[4])));
	printf("ft_read\t : %s\t| ret = %zd\n", str2, ft_read(fd2, str2, atoi(argv[4])));
	free(str1);
	free(str2);
	close(fd1);
	close(fd2);
	return (EXIT_SUCCESS);
}

int	test_strdup(int argc, char *argv[])
{
	char *ret1;
	char *ret2;

	if (argc <= 2)
	{
		printf(ERROR_NEED_ARG);
		return (EXIT_SUCCESS);
	}
	printf("strdup\t\t: %s\n", ret1 = strdup(argv[2]));
	printf("ft_strdup\t: %s\n", ret2 = ft_strdup(argv[2]));
	argv[2][0] = '8';
	printf("Modified arg\t: %s\n", ret2);
	free(ret1);
	free(ret2);
	return (EXIT_SUCCESS);
}

int main(int argc, char *argv[])
{
	if (argc <= 1)
	{
		printf(ERROR_ARG);
		return (EXIT_SUCCESS);
	}
	if (strcmp(argv[1], "strlen") == 0)
		test_strlen(argc, argv);
	else if (strcmp(argv[1], "strcpy") == 0)
		test_strcpy(argc, argv);
	else if (strcmp(argv[1], "strcmp") == 0)
		test_strcmp(argc, argv);
	else if (strcmp(argv[1], "write") == 0)
		test_write(argc, argv);
	else if (strcmp(argv[1], "read") == 0)
		test_read(argc, argv);
	else if (strcmp(argv[1], "strdup") == 0)
		test_strdup(argc, argv);
	else
		printf(ERROR_FUNC_UNKNOW);
	return(EXIT_SUCCESS);
}
