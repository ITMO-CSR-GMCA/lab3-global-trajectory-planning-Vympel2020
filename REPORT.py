*** MINISTRY OF SCIENCE AND HIGHER EDUCATION OF THE RUSSIAN FEDERATION
ITMO UNIVERSITY, St. PETERSBUG, RUSSIA
	
 
 
Table of Contents
Report: Robot Path Planning Using Potential Fields	1
2.	Methodology:	1
3.	OUTPUT	1
4.	RESULTS	1
5.	CONCLUSION	1






Report On: Robot Path Planning Using Potential Fields
a.	OBJECTIVE
To simulate and visualize a robot navigating from a start point (START) to a desired point (GOAL) while avoiding obstacles using the Artificial Potential Field method.

1.	METHODOLOGY
1.1	Grid Setup:
The environment is represented by A 2D grid of size 100x100, created using NumPy.
1.2	Start and Goal Points:
•	The robot starts at (10, 10) and aims to reach the goal at (90, 90).

1.3	Obstacles:
•	The environment contains circular and rectangular obstacles defined by their positions and sizes.

1.4	Potential Fields:
i.	Attractive Potential: Pulls the robot toward the goal.
ii.	Repulsive Potential: Pushes the robot away from nearby obstacles.
iii.	Total Potential Field: This combines the attractive and repulsive potentials. It defines the energy landscape of the system.

1.5	Gradient Descent Path Planning:
•	The robot moves by following the negative gradient of the total potential (i.e., downhill on the energy landscape).
•	Movement continues until the robot reaches close to the goal or the gradient becomes too small to proceed.

2.	OUTPUT RECORDING AND VISUALIZATION
a)	The robot's path is saved to a CSV file.
b)	A visualization is created showing:
i.	The energy landscape (as a contour map),
ii.	Obstacles,
iii.	Start and goal points,
iv.	The planned path,
v.	An animated dot representing the robot’s motion.


3.	RESULTS
•	The robot successfully navigated toward the goal while avoiding obstacles.
•	The planned path is smooth and keeps to the environment's constraints.
•	The animation provides an intuitive visualization of how potential fields guide motion.
4.	CONCLUSION
The task successfully demonstrates robot path planning using artificial potential fields in a 2D space. The simulation visualizes both the theoretical landscape and the resulting trajectory, offering insight into how local gradients and obstacle proximity influence motion.
