from db.database import Base, engine
from models import job  # models load karna zaroori hai

# 🔥 CREATE ALL TABLES HERE
Base.metadata.create_all(bind=engine)

print("✅ Database + Tables Created Successfully!")