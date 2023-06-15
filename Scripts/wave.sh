#!/bin/bash

# List of paths to Docker Compose files for list 1
compose_paths_2=(
  # Add more paths here
)

compose_paths_1=(
  "./web/bigHEAD/docker-compose.yml"
  "./web/fREe/docker-compose.yml"
  "./web/Inspector/docker-compose.yml"
  "./web/PingPong1/docker-compose.yml"
  "./web/PingPong2/docker-compose.yml"
  "./misc/matrix/docker-compose.yml"
)


# Check if an integer argument was passed
if [[ ! $1 =~ ^[0-9]+$ ]]; then
  echo "Please provide an integer argument."
  exit 1
fi

# Choose the list of paths based on the input integer
if (( $1 == 1 )); then
  compose_paths=("${compose_paths_1[@]}")
elif (( $1 == 2 )); then
  compose_paths=("${compose_paths_2[@]}")

else
  echo "Invalid integer argument. Please choose 1 or 2."
  exit 1
fi

# Iterate through the list of Docker Compose paths and run docker-compose up
for path in "${compose_paths[@]}"; do
  echo "Running Docker Compose for $path"
  docker-compose -f "$path" up --build -d
done
