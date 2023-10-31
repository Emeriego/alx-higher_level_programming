#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 *  * main - check the code
 *   *
 *    * Return: Always 0.
 *     */
int main(void)
{
	    listint_t *head;
	        listint_t *current;
		    listint_t *temp;
		        int i;

			    head = NULL;
			        myaddNodeint(&head, 0);
				    myaddNodeint(&head, 1);
				        myaddNodeint(&head, 2);
					    myaddNodeint(&head, 3);
					        myaddNodeint(&head, 4);
						    myaddNodeint(&head, 98);
						        myaddNodeint(&head, 402);
							    myaddNodeint(&head, 1024);
							        myprintListint(head);

								    if (check_cycle(head) == 0)
									            printf("Linked list has no cycle\n");
								        else if (check_cycle(head) == 1)
										        printf("Linked list has a cycle\n");

									    current = head;
									        for (i = 0; i < 4; i++)
											        current = current->next;
										    temp = current->next;
										        current->next = head;

											    if (check_cycle(head) == 0)
												            printf("Linked list has no cycle\n");
											        else if (check_cycle(head) == 1)
													        printf("Linked list has a cycle\n");

												    current = head;
												        for (i = 0; i < 4; i++)
														        current = current->next;
													    current->next = temp;

													        free_listint(head);

														    return (0);
}
