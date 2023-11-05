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
	listint_t *slow = *head, *fast = *head;
	listint_t *next = NULL, *prev = NULL;
	listint_t *left = NULL, *right = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/*Find the middle*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	/*Reverse the second part of the list*/
	prev->next = NULL;
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	/*Find palindrome*/
	left = *head;
	right = prev;
	while (left != NULL && right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}
	return (1);
}
