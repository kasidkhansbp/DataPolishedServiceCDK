import aws_cdk as core
import aws_cdk.assertions as assertions

from data_polished_service_cdk.data_polished_service_cdk_stack import DataPolishedServiceCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in data_polished_service_cdk/data_polished_service_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DataPolishedServiceCdkStack(app, "data-polished-service-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
