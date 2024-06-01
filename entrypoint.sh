#!/bin/sh

if [ "$RUN_TESTS" = "true" ]; then
  echo "Running tests..."
  python3 -m unittest discover -s tests
else
  echo "Skipping tests. Running main application..."
  exec python3 main.py "$@"
fi