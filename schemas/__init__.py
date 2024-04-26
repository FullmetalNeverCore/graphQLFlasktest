import graphene 
from graphene_sqlalchemy import SQLAlchemyConnectionField,SQLAlchemyObjectType
from db import User as UserDBmodel,Posts as PostsDBmodel,Session


class UserScheme(SQLAlchemyObjectType):
    class Meta:
        model = UserDBmodel
        interfaces = (graphene.relay.Node,)


class PostSchema(SQLAlchemyObjectType):
    class Meta:
        model = PostsDBmodel
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserScheme)
    all_posts = SQLAlchemyConnectionField(PostSchema)


schema = graphene.Schema(query=Query)