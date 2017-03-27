#!/bin/sh

. /etc/sysconfig/heat-params

echo "notifying heat"

VERIFY_CA_ARG="-k"
if [ "$VERIFY_CA" == "True" ]; then
    VERIFY_CA_ARG=""
fi

STATUS="SUCCESS"
REASON="Setup complete"
DATA="OK"
UUID=`uuidgen`

data=$(echo '{"Status": "'${STATUS}'", "Reason": "'$REASON'", "Data": "'${DATA}'", "Id": "'$UUID'"}')

curl "$VERIFY_CA_ARG" -i -X POST -H "Content-Type: application/json" -H "X-Auth-Token: $WAIT_HANDLE_TOKEN" \
    --data-binary "'$data'" \
    "$WAIT_HANDLE_ENDPOINT"
