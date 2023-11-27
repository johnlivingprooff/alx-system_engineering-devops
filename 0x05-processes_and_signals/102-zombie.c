#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - runs a while loop infinately
 * Return: 0 - Success
*/
int infinite_while(void)
{
    while (1)
        sleep(1);
    return (0);
}

/**
 * main - creates 5 zombie processes
 * @n: number of processes created
 * Return: Exit Success!
*/
int main(void)
{
    pid_t child;
    int id = 5, i;

    for (i = 0; i < id; i++)
    {
        child = fork();

        if (child >= 0)
        {
            if (child == 0)
            {
                printf("Zombie process created, PID: %d\n", getpid());
                sleep(2); /*prints within a 1 sec interval*/
                exit(0);
            }
        }

        else
            exit(EXIT_FAILURE);
    }

    infinite_while();

    return(0);
}