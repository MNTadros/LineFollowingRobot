# Line Following Robot

This repository contains the **Line Following Robot** project, a visual follow-line exercise from the [Robotics Academy](https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/). The project demonstrates how to use computer vision and control algorithms to autonomously follow a line.

## Getting Started

### Prerequisites

Ensure you have [Docker](https://www.docker.com/) installed on your system.

### Installation and Launch

Run the following command to start the simulation environment:

```bash
docker run --rm -it -p 8000:8000 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 -p 7163:7163 jderobot/robotics-academy
```

Once the container is running, open your browser and navigate to:

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Select the **Follow Line** exercise from the interface.

### Running the Simulation

1. Wait for the **Connect** button to turn green and display "Connected."
2. Click the **Launch** button and wait until an alert appears with the message "Connection Established," and the button displays "Ready."
3. Upload your code using the **Load File** option or paste it directly into the text editor.
4. Press the **Load in Robot** button and click **Play** to start the simulation.

## Features

- **Real-time Line Detection**: Uses computer vision to detect and follow a line.
- **Customizable Control**: Modify the control parameters to experiment with different behaviors.
- **Interactive Interface**: Upload and test your code directly in the simulation environment.

## Demo

Check out the demo video to see the Line Following Robot in action!

The demo is running at 3X speed for a better viewing experience.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/dnI6DV_M8ws" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

For more details, visit the [Robotics Academy documentation](https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/).