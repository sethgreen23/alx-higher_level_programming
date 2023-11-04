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
	int length = 0, i = 0, j = 0, flag = 0, *tab = NULL;
	listint_t *pointer = *head;

	if (head == NULL)
		return (1);
	while (pointer != NULL)
	{
		length++;
		pointer = pointer->next;
	}
	tab = malloc(sizeof(int) * (length + 1));
	if (tab == NULL)
		return (0);
	pointer = *head;
	while (pointer != NULL)
	{
		tab[i++] = pointer->n;
		pointer = pointer->next;
	}
	flag = 1;
	i = 0, j = length - 1;
	for (; i < j; i++, j--)
	{
		if (tab[i] != tab[j])
		{
			flag = 0;
			break;
		}
	}
	free(tab);
	return (flag);
}
