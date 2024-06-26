import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    goodbye = graphene.String()


    def resolve_hello(root,info,name):
        return f'Hello {name}'
    
    def resolve_goodbye(root,info):
        return 'Goodbye'
    