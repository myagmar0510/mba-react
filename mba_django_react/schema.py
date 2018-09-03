import graphene

import mba.api.testschema
from mba.api import testschema as TestSchema

class Query(
    TestSchema.Query,
    graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)