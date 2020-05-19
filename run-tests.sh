#!/bin/bash

# it seems it does not work well if using echo for function return value, and calling inside $() (is a subprocess spawned?)
function wait_and_get_exit_codes() {
    children=("$@")
    EXIT_CODE=0
    for job in "${children[@]}"; do
       echo "PID => ${job}"
       CODE=0;
       wait ${job} || CODE=$?
       if [[ "${CODE}" != "0" ]]; then
           echo "At least one test failed with exit code => ${CODE}" ;
           EXIT_CODE=1;
       fi
   done
}

DIRN=$(dirname "$0");

commands=(
    "{ python -m unittest tests.testKey; }"
    "{ python -m unittest tests.testBalance; }"
    "{ python -m unittest tests.testBoleto; }"
    "{ python -m unittest tests.testBoletoLog; }"
    "{ python -m unittest tests.testBoletoPayment; }"
    "{ python -m unittest tests.testBoletoPaymentLog; }"
    "{ python -m unittest tests.testEvent; }"
    "{ python -m unittest tests.testTransaction; }"
    "{ python -m unittest tests.testTransfer; }"
    "{ python -m unittest tests.testTransferLog; }"
    "{ python -m unittest tests.testUtilityPaymentLog; }"
    "{ python -m unittest tests.testUtilityPayment; }"
    "{ python -m unittest tests.testWebhook; }"
    )

clen=`expr "${#commands[@]}" - 1` # get length of commands - 1

children_pids=()
for i in `seq 0 "$clen"`; do
    (echo "${commands[$i]}" | bash) &   # run the command via bash in subshell
    children_pids+=("$!")
    echo "$i ith command has been issued as a background job"
done
# wait; # wait for all subshells to finish - its still valid to wait for all jobs to finish, before processing any exit-codes if we wanted to
#EXIT_CODE=0;  # exit code of overall script
wait_and_get_exit_codes "${children_pids[@]}"

echo "EXIT_CODE => $EXIT_CODE"
sleep 5
exit "$EXIT_CODE"
# end
