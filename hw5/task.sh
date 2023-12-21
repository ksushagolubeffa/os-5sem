#!/bin/bash

RED='\e[31m'
GREEN='\e[32m'
RESET='\e[0m'

declare -i step=1
declare -i hits=0
declare -i misses=0
declare -a last_numbers=()

while true; do
    echo -e "Step: ${step}"

    read -p "Please enter number from 0 to 9 (q - quit): " user_input

    if [[ "${user_input}" == "q" ]]; then
        echo "Bye"
        exit 0
    fi

    if [[ "${user_input}" =~ ^[0-9]$ ]]; then
        script_number=$(( RANDOM % 10 ))

        if (( script_number == user_input )); then
            echo -e "Hit! My number: ${script_number}"
            hits+=1
            ans_color="${GREEN}${script_number}${RESET}"
        else
            echo -e "Miss! My number: ${script_number}"
            misses+=1
            ans_color="${RED}${script_number}${RESET}"
        fi

        last_numbers=("${last_numbers[@]}" "${ans_color}")

        hit_percent=$(( hits * 100 / step ))
        miss_percent=$(( 100 - hit_percent ))

        echo -e "Hit: ${hit_percent}%, Miss: ${miss_percent}%"

        if (( "${#last_numbers[@]}" >= "10")); then
            echo -e "Numbers: ${last_numbers[@]: -10}"
        fi

        step+=1
    else
        echo "Not a valid input. Please repeat."
    fi
done
