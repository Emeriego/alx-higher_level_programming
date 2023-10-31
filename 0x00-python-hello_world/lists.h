#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct listint_s - the list to be worked with
 * @n: member int
 * @next: this points2next node
 */
typedef struct listint_s
{
	    int n;
	    struct listint_s *next;
} listint_t; //listint_t

size_t myprintListint(const listint_t *h);
listint_t *myaddNodeint(listint_t **head, const int n);
void myfreeListint(listint_t *head);
int check_cycle(listint_t *list);
#endif
