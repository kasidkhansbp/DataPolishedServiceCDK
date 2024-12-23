from constructs import Construct
from aws_cdk import Stage

from data_polished_service_cdk.data_polished_service_cdk_stack import DataPolishedServiceCdkStack


class AppStages(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        DataPolishedServiceCdkStack(self,"DataPolishedServiceCdkStack")
