# kafka

the library is confluent-kafka

You will need to instantiate a consumer.
Add config - topic, date, partition, group id, offset date, etc

## poll

polling mean to actively request messages from broker. nifi polls kafka. kafka uses a pull based system where the consumers all request data.

## push or pull

kafka never push data

## Compared to tradition

compared to traditional message queue, kafka can retain their message for a preset amount of time.

It supports event messaging and not just simple messaging.

Allows independent consumer.
