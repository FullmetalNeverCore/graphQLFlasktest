import flask
from flask_graphql import GraphQLView
import graphene
import queries.query as q
from schemas import schema

app = flask.Flask(__name__)


app.add_url_rule(
    '/graphQL',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

@app.route("/")
def main():
    exec = schema.execute('''
        {
        allUsers{
            edges{
            node{
                uname
            }
            }
        }
        }
        ''')
    return flask.jsonify(dict(exec.data))
    

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8080)
