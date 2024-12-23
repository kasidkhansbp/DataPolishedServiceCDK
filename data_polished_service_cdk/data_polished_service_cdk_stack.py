from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_s3_notifications as s3_notification,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_lambda_event_sources as lambda_event_sources
)
from constructs import Construct

class DataPolishedServiceCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        my_bucket = s3.Bucket(self,"MyBucket")

        dlq = sqs.Queue(self, "MyDLQ")

        my_queue = sqs.Queue(self, "MyQueue", dead_letter_queue=sqs.DeadLetterQueue(max_receive_count=5))

        #Enable notifications for the bucket
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED,s3_notification.SqsDestination(my_queue))

        lambda_function = _lambda.Function(self, "myFunction",
            runtime =_lambda.Runtime.PYTHON_3_8,
            handler = "index.handler",
            code=_lambda.Code.from_asset("lambda/"))

        #Create a dynamoDB table
        dynamo_table = dynamodb.Table(self, "PolishedDataDBTable",
                                      partition_key=dynamodb.Attribute(name="Id",
                                    type=dynamodb.AttributeType.STRING), read_capacity=5,write_capacity=5)

        # Grant the Lambda function permissions to write to DynamoDB
        dynamo_table.grant_write_data(lambda_function)
        # Grant the lambda function to read data from S3 file
        my_bucket.grant_read(lambda_function)

        #Connect SQS to Lambda ( SQS to Lambda )
        lambda_function.add_event_source(lambda_event_sources.SqsEventSource(my_queue))
