#!/bin/bash

BOLD="\033[1m"
RESET="\033[0m"

echo
echo "---------------------------------------------------------------"
echo -e "${BOLD}Running formatting check with 'black'${RESET}"
black --check .

echo
echo "---------------------------------------------------------------"
echo -e "${BOLD}Running import order check with 'isort'${RESET}"
isort --check .

echo
echo "---------------------------------------------------------------"
echo -e "${BOLD}Running static type check with 'mypy'${RESET}"
mypy --check promclient

echo
