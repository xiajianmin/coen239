#include <stdio.h> /* printf, perror */
#include <string.h> /* strcpy, strstr */
#include <stdlib.h> /* exit */
#include <stdbool.h> /* true, false */
#include <math.h> /* INFINITY, -INFINITY */

#define inf 99999
#define V 6 // number of vertices

int dGraph[V][V] = {
		{inf, 1, 2, inf, inf, inf},
		{inf, inf, 5, 7, inf, inf},
		{inf, inf, inf, 1, 2, inf},
		{inf, inf, inf, inf, inf, 2},
		{inf, inf, 8, 3, inf, 5},
		{inf, inf, inf, 9, inf, inf},
	};

// d = {0, 1, 2, 3, 4, 5}
// p = {0, 1, 1, 3, 3, 4}

int top = 0; // keep track of the top element of stack
int end = 0; // keep track of the end element of stack

/**
 *	Push 
 */
void push(int stack[], int el) {
	// if stack is not full
	if (end != (V-1)) {
		stack[end] = el;
		end++;
	}
}

/**
 *	Pop
 */
int pop(int stack[]) {
	int ret;
	ret = stack[top];
	top++;
	return ret;
}

void printDistance(int d[]) {
	int i;
	printf("Distance: (");
	for (i=0; i<V; i++) {
		if (i == V-1) {
			printf("%d)\n", d[i]);
			break;
		}
		printf("%d, ", d[i]);
	}
}

void printPrevious(int p[]) {
	int i;
	printf("Precedence: (");
	for (i=0; i<V; i++) {
		if (i == V-1) {
			printf("%d)\n", p[i]+1);
			break;
		}
		printf("%d, ", p[i]+1);
	}
}

void printUnvisited(int p[]) {
	int i;
	printf("Unvisited: (");
	for (i=0; i<V; i++) {
		if (i == V-1) {
			printf("%d)\n", p[i]+1);
			break;
		}
		printf("%d, ", p[i]+1);
	}
}

/**
 *	Dijkstra algorithm
 */
void dijkstra(int graph[][V], int src) {
	int distance[V], prev[V], unvisited[V] = {0, 1, 2, 3, 4, 5}, min, i, cur;
	// Set all distance to infinity and precedence to null.
	for (i=0; i<V; i++) {
		distance[i] = inf;
		prev[i] = (int)NULL;
	}

	// push source vertices to stack
	push(unvisited, src);
	printf("INITIAL VALUE\n");
	printDistance(distance);
	printPrevious(prev);
	printUnvisited(unvisited);
	while (top != V) {
		cur = pop(unvisited);
		printf("Iteration %d\n", cur);
		// checking distance between vertices
		for (i=cur; i<V; i++) {
			// if self
			if (i == src) {
				distance[i] = 0;
				prev[i] = -1;
				continue;
			}

			if (i != cur) {
				// add distance from vertex[i] to connected vertices
				if (distance[i] != inf) {
					min = distance[cur] + graph[cur][i];
					if (distance[i] > min) {
						distance[i] = min;
						prev[i] = cur;
					}
				} else {
					distance[i] = distance[cur] + graph[cur][i];
					prev[i] = cur;
				}
			}
		}
		printDistance(distance);
		printPrevious(prev);
		printUnvisited(unvisited);
	}
}

/**
 *
 */
int main(int argc, char **argv)
{
	int src=1;
	// if (argc > 1) {
	// 	// only the source is provided
	// 	src = (int) argv[0];
	// }

	dijkstra(dGraph, src-1);

	return 0;
}
