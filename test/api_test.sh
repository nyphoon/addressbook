TEST_DIR="api_test"
RESULT_FILE="result.txt"
SERVER_URL='localhost:5000/api/addrbook'


rm -r $TEST_DIR
mkdir $TEST_DIR
pushd $TEST_DIR


ADDR_ID=1
touch $RESULT_FILE

echo "CREATE:" >> $RESULT_FILE
curl \
--request PUT ${SERVER_URL} \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Alice",
    "email": "alice@cyberpunk.com",
    "phone": "100100100",
    "address": "Cyber St. No. 100"
}' \
>> $RESULT_FILE

echo "GET:" >> $RESULT_FILE
curl \
--request GET ${SERVER_URL}/${ADDR_ID} \
--header 'Content-Type: application/json' \
>> $RESULT_FILE

echo "UPDATE:" >> $RESULT_FILE
curl \
--request POST ${SERVER_URL}/${ADDR_ID} \
--header 'Content-Type: application/json' \
--data-raw '{
    "phone": "11111111111"
}' \
>> $RESULT_FILE

echo "GET:" >> $RESULT_FILE
curl \
--request GET ${SERVER_URL}/${ADDR_ID} \
--header 'Content-Type: application/json' \
>> $RESULT_FILE

echo "LIST:" >> $RESULT_FILE
curl ${SERVER_URL} >> $RESULT_FILE

echo "DELETE:" >> $RESULT_FILE
curl \
--request DELETE ${SERVER_URL}/${ADDR_ID} \
>> $RESULT_FILE

echo "GET:" >> $RESULT_FILE
curl \
--request GET ${SERVER_URL}/${ADDR_ID} \
--header 'Content-Type: application/json' \
>> $RESULT_FILE

popd