#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <string.h>

/**
 * insert_node - insert node
 * @head: head
 * @number: number
 *
 * Return: new created list or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	temp = *head;
	if (temp == NULL)
		return (NULL);
	if (temp->n >= number)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (temp->next != NULL)
	{
		if (temp->next->n >= number)
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
				return (NULL);
			new_node->n = number;
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	temp->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
