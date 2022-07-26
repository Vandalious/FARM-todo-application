from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from todo import Todo


# the api object
app = FastAPI()

#import database functions
from database import (
    fetch_one_todo,
    fetch_all_todos,
    insert_todo,
    update_todo,
    remove_todo
)

# permissions with React
origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods = ['*'],
    allow_headers = ['*']
)


# routes
@app.get('/')
def home():
    return {'Ping': 'Pong'}


# get all TODOs
@app.get('/api/todo')
async def get_todo():
    response = await fetch_all_todos()
    return response


# get a single TODO by title
@app.get('/api/todo{title}', response_model=Todo)
async def get_todo_by_title(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'There is no TODO item with the title "{title}".')


# create a TODO
@app.post('/api/todo', response_model=Todo)
async def post_todo(todo: Todo):
    title_len = len(todo.title)
    detail_len = len(todo.detail)
    if title_len > 12 or title_len == 0 or detail_len > 300 or detail_len == 0:  # data validation
        raise HTTPException(400, 'Something went wrong / Bad Request')
    
    response = await insert_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong / Bad Request!')


# update a TODO by title
@app.put('/api/todo{title}', response_model=Todo)
async def put_todo(title: str, detail: str, priority: str, is_done: bool):
    response = await update_todo(title, detail, priority, is_done)
    if response:
        return response
    raise HTTPException(404, f'There is no TODO item with the title "{title}".')


# delete a TODO by title
@app.delete('/api/todo{title}')
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return 'Successfully deleted TODO item!'
    raise HTTPException(404, f'There is no TODO item with the title "{title}".')
