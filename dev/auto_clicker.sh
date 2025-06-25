#!/bin/bash

# Replace with your actual window ID
WINDOW_ID=35654233

# Coordinates inside the window (relative to top-left of tab)
X=1132
Y=602

# Interval between clicks (in seconds)
INTERVAL=5

echo "Clicking in background window $WINDOW_ID at ($X, $Y)... Press Ctrl+C to stop."
while true; do
    xdotool windowactivate --sync $WINDOW_ID mousemove --window $WINDOW_ID $X $Y click 1
    sleep $INTERVAL
done
