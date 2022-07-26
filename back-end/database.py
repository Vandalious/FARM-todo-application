from todo import Todo
import motor.motor_asyncio  # MongoDB Driver


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.todo_db
collection = db.todo


async def fetch_one_todo(title: str):
    document = await collection.find_one({'title': title})
    return document

async def fetch_all_todos():
    todos = [Todo(**document) async for document in collection.find({})]
    
    # the above code is equal to this:
    '''todos = []
       cursor = collection.find({})
       async for document in cursor:
           todos.append(Todo(**document))'''

    return todos

async def insert_todo(todo: Todo):
    await collection.insert_one(todo)
    return todo

async def update_todo(title: str, detail: str, priority: str, is_done: bool):
    await collection.update_one({'title': title}, {'$set': {'detail': detail, 'priority': priority, 'is_done': is_done}})
    document = await collection.find_one({'title': title})
    return document

async def remove_todo(title: str):
    document = await collection.delete_one({'title': title})
    if document.deleted_count:
        return True
    return False
