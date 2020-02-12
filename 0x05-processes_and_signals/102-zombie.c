#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 *infinite_while - infinite while loop
 *Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 *main - 5 zombie processes
 *Return: 0
 */
int main(void)
{
	int i = 0;
	int process;

	while (i < 5)
	{
		process = fork();
		if (process == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n",
				getpid());
			return (0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
