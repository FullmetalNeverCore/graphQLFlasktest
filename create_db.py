from db import User,Posts,Base,engine

Base.metadata.create_all(bind=engine)

print("Done.")