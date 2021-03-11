from peewee import *

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('libraryapp', user='root', password='',
                         host='localhost', port=3306)

class Books(Model):
    title = CharField()
    description = TextField()
    category = ForeignKeyField(Category, backref='category')
    code = CharField()
    part_order = IntegerField()
    price = DecimalField()
    publisher = ForeignKeyField(Publisher, backref='publisher')
    author = ForeignKeyField(Author, backref='author')
    image = CharField()
    status = CharField()
    date = DateTimeField()

class Clients(Model):
    name = CharField()
    mail = CharField()
    phone = CharField()
    date = DateTimeField()
    National_ID = IntegerField()

class Employee(Model):
    name = CharField()
    mail = CharField()
    phone = CharField()
    date = DateTimeField()
    National_ID = IntegerField()
    periority = IntegerField()

class Category(Model):
    category_name = CharField()
    # parent_category = Recursive relationshio

class Branch(Model):
    name = CharField()
    code = CharField()
    location = CharField()

class Daily_Movements(Model):
    book = ForeignKeyField(Books, backref='daily_book')
    client = ForeignKeyField(Clients, backref='book_client')
    type = CharField() # rent or retrive
    date = DateTimeField()
    branch = ForeignKeyField(Branch, backref='Daily_branch')
    Book_from = DateField() 
    Book_to = DateField()
    user = 

class History(Model):
    pass

class Publisher(Model):
    pass

class Author(Model):
    pass


db.connect()
db.create_tables([Books, Clients, Employee, Category, Branch, Daily_Movements, History, Publisher])