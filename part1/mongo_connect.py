from mongoengine import connect

uri = "mongodb+srv://boris:test123@cluster0.1lmlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

connect(host=uri, ssl=True)
   
