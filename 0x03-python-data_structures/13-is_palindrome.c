#include "lists.h"

listint_t *reverse_listint(listint_t **h);
int is_palindrome(listint_t **h);

/**
 * reverse_listint - func reverses a list.
 * @h: ptr to starting n.
 * Return: returns ptr to the h of the reversed list.
 */
listint_t *reverse_listint(listint_t **h)
{
	listint_t *n = *h, *next, *prev = NULL;

	while (n != NULL)
	{
		next = n->next;
		n->next = prev;
		prev = n;
		n = next;
	}
	*h = prev;
	return (*h);
}

/**
 * is_palindrome -  func Ccecks if list is palindrome.
 * @h: pointer to the h of the list.
 * Return: returns 1.
 */
int is_palindrome(listint_t **h)
{
	listint_t *tempy, *rev, *mid;
	size_t sz = 0, i;

	if (*h == NULL || (*h)->next == NULL)
	{
		return (1);
	}
	tempy = *h;
	while (tempy)
	{
		sz++;
		tempy = tempy->next;
	}

	tempy = *h;
	for (i = 0; i < (sz / 2) - 1; i++)
	{
		tempy = tempy->next;
	}
	if ((sz % 2) == 0 && tempy->n != tempy->next->n)
		return (0);

	tempy = tempy->next->next;
	rev = reverse_listint(&tempy);
	mid = rev;
	tempy = *h;
	while (rev)
	{
		if (tempy->n != rev->n)
			return (0);
		tempy = tempy->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
