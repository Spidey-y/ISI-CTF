#!/bin/bash

# List of paths to Docker Compose files for list 1
compose_paths_2=(
  "./crypto/int_game/docker-compose.yml"
  "./misc/ChekkaBot/docker-compose.yml"
  "./pwn/notes_keeper_II/docker-compose.yml"
  "./web/Akatsuki/docker-compose.yml"
  "./web/Magic_links/docker-compose.yml"
  "./web/token/docker-compose.yml"
  "./pwn/simple/docker-compose.yml"
  "./pwn/Auth/docker-compose.yml"
  # Add more paths here
)

compose_paths_1=(
  "./rev/Debug/docker-compose.yml"
  "./web/Bad_PHP/docker-compose.yml"
  "./web/say_my_name/docker-compose.yml"
  "./web/SoS/docker-compose.yml"
  "./pwn/BOF_scanf/docker-compose.yml"
  "./pwn/weird/docker-compose.yml"
  "./pwn/ret2win_II/docker-compose.yml"
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
