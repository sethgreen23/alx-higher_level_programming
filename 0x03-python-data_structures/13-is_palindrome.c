#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - is linked list a palindrome
 * @head: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
	int length = 0, i = 0, sum = 0, stop = 0;
	listint_t *pointer = *head;

	if (head == NULL)
		return (1);
	while (pointer != NULL)
	{
		length++;
		pointer = pointer->next;
	}
	stop = length / 2, i = 0, sum = 0;
	pointer = *head;
	while (pointer != NULL)
	{
		if (i == stop && (length % 2 == 1))
		{
			pointer = pointer->next;
			i++;
			continue;
		}
		if (i < stop)
			sum += pointer->n;
		else
			sum -= pointer->n;
		pointer = pointer->next;
		i++;
	}
	return (sum == 0 ? 1 : 0);
}
