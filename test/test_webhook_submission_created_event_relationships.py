# coding: utf-8

"""
    Bugcrowd REST API

    This is Bugcrowd's primary REST API and follows the [JSON API specification](https://jsonapi.org/format/).  For more information on how to get started check out the [usage documentation](https://docs.bugcrowd.com/api/usage/) 

    The version of the OpenAPI document: 2024-01-11
    Contact: support@bugcrowd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from bugcrowd_client.models.webhook_submission_created_event_relationships import WebhookSubmissionCreatedEventRelationships

class TestWebhookSubmissionCreatedEventRelationships(unittest.TestCase):
    """WebhookSubmissionCreatedEventRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookSubmissionCreatedEventRelationships:
        """Test WebhookSubmissionCreatedEventRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookSubmissionCreatedEventRelationships`
        """
        model = WebhookSubmissionCreatedEventRelationships()
        if include_optional:
            return WebhookSubmissionCreatedEventRelationships(
                actor = bugcrowd_client.models.webhook_submission_created_event_relationships_actor.WebhookSubmissionCreatedEvent_relationships_actor(
                    data = bugcrowd_client.models.event_relationships_actor_data.Event_relationships_actor_data(
                        type = 'identity', 
                        id = '', ), 
                    links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                        related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                            href = '', ), ), ),
                resource = bugcrowd_client.models.webhook_submission_created_event_relationships_resource.WebhookSubmissionCreatedEvent_relationships_resource(
                    data = bugcrowd_client.models.webhook_submission_created_event_relationships_resource_data.WebhookSubmissionCreatedEvent_relationships_resource_data(
                        type = 'submission', 
                        id = '', ), 
                    links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                        related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                            href = '', ), ), )
            )
        else:
            return WebhookSubmissionCreatedEventRelationships(
                actor = bugcrowd_client.models.webhook_submission_created_event_relationships_actor.WebhookSubmissionCreatedEvent_relationships_actor(
                    data = bugcrowd_client.models.event_relationships_actor_data.Event_relationships_actor_data(
                        type = 'identity', 
                        id = '', ), 
                    links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                        related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                            href = '', ), ), ),
                resource = bugcrowd_client.models.webhook_submission_created_event_relationships_resource.WebhookSubmissionCreatedEvent_relationships_resource(
                    data = bugcrowd_client.models.webhook_submission_created_event_relationships_resource_data.WebhookSubmissionCreatedEvent_relationships_resource_data(
                        type = 'submission', 
                        id = '', ), 
                    links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                        related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                            href = '', ), ), ),
        )
        """

    def testWebhookSubmissionCreatedEventRelationships(self):
        """Test WebhookSubmissionCreatedEventRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()