# Traveling Salesman Problem
Project of the Graphs discipline, implementation in Python of the Traveling Salesman Problem (TSP). The Traveling Salesman Problem is a problem that tries to determine the shortest route to travel through a series of cities (visiting each one only once), returning to the city of origin. It is an NP-hard optimization problem inspired by the need for sellers to deliver to different locations (cities) in the shortest possible way, reducing travel time and possible transportation and fuel costs.

## Operation
To use the code, just run the main file and the dataset graphs will be processed and printed in the terminal. You must have Python 3+ installed.

## Results
In the results of the databases, in terms of path costs resulting from the three heuristics implemented to solve the problem (Bellmore & Nemhauser, Twice-Around and Christofides), it can be seen that it is not possible to know for sure which heuristic will result in the lowest cost. In some databases and examples, the Bellmore & Nemhauser heuristic presented the lowest cost cycles, while in others the winner was the Christofides heuristic or Twice-Around.

This uncertainty in the cycle cost of the three heutirstics is due to the fact that the performance of each one can vary according to the graph. In addition, the algorithms contain random components, which can generate cycles of different costs in different executions.

A curious result is found in the output of the pd01_d.txt database. The minimum cost of the Hamiltonian cycle of the Bellmore & Nemhauser heuristic was 291, which is the smallest possible cycle in the graph, described in the database link.

Another interesting point to note is that, in the bibliography it is explained that Christofides' heuristic guarantees that the solution produced by his algorithm is at most 1.5 times worse than the optimal solution of the problem. It is possible to verify this fact in the figures, analyzing the costs of this heuristic and comparing them with the minimum costs presented in the database.

In terms of execution time, a more constant result was obtained. In general, it is possible to observe that the Bellmore & Nemhauser heuristic was the fastest, while Twice-Around and Christofides' heuristic had similar times.

Analyzing the complexity of the heuristic, it can be deduced that the runtime results are coherent. The Bellmore & Nemhauser heuristic, being the simplest and most direct, presented the fastest results, even having the same complexity as the Twice-Around (O(n²)).

Between the Twice-Around (O(n²)) and the Christofides heuristic (O(n³)), in most cases the execution time followed the logic of complexity, that is, the Christofides heuristic was slower. However, in some graphs it is possible to analyze in the figures that Twice-Around took even longer than Christofides. To address this issue, more runtime meters were placed on each specific part of the algorithms.

The result of this verification was that, even though the Christofides heuristic was more complex because it was dominated by perfect-matching, the Hierholzer algorithm took longer to run in Twice-Around, precisely because the trees had their edges bent. Therefore, in the practical example, that is, in the average case, in some situations the Hierholzer algorithm ended up dominating the execution time of the algorithms.

## References
- TSP: https://en.wikipedia.org/wiki/Travelling_salesman_problem
- GOLDBARG, Marco; GOLDBARG, Elizabeth. Grafos: conceitos, algoritmos e aplicações. Rio de Janeiro: Elsevier, 2012.
- TSP Data for the Traveling Salesperson Problem: https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
