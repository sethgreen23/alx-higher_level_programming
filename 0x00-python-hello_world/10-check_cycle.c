#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * save_list - save list in the array
 * @list_array: array of nodes
 * @head: current element in the list
 * @size: size of the array
 *
 * Return: new allocated array
*/
listint_t **save_list(listint_t **list_array, listint_t *head, int size)
{
	int i;
	listint_t **new_list = NULL;

	new_list = malloc(sizeof(listint_t *) * (size + 1));

	if (new_list == NULL)
	{
		free(new_list);
		free(list_array);
	}
	for (i = 0; i < size; i++)
		new_list[i] = list_array[i];
	new_list[i] = head;
	free(list_array);
	return (new_list);
}
/**
 * check_cycle - check cycle in single linked list
 * @list: list
 *
 * Return: 0 if no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t **list_array = NULL;
	int i = 0, size = 0;

	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		for (i = 0; i < size; i++)
		{
			if (list == list_array[i])
			{
				return (1);
			}
		}
		list_array = save_list(list_array, list, size);
		size++;
		list = list->next;
	}
	return (0);
}

