from fastapi import FastAPI #import

api = FastAPI()  #instance

# simulated data base given bellow
all_todo = [
    {'tid':1,'name':'game', 'desc':'Go game'},
    {'tid':2,'name':'movie', 'desc':'Go movie'},
    {'tid':3,'name':'book', 'desc':'Go book'},
    {'tid':4,'name':'clg', 'desc':'Go clg'},
    {'tid':5,'name':'music', 'desc':'Go music'}
]

#GET POST PUT DELETE
# get to get some infor or details
# post to submit to server
# put change something existing
# delete to delete

@api.get('/')  #decorate
def index(): #function
    return {'Message' : 'Hello World'}

@api.get('/todos/{tid}')
def get_todo(tid:int):
    for todo in all_todo :
        if todo['tid'] == tid:
            return {'result' : todo}


#we need to mention datatype else we type cast input into str
@api.get('/todos')
def get_todos(first_n :int = None):
    if first_n:
        return all_todo[:first_n]
    else :
        return all_todo


@api.post('/todos')
def create_todo (todo : dict) :
    new_tid = max(todo['tid']for todo in all_todo)+1

    new_todo = {
        'tid' : new_tid,
        'name' : todo ['name'],
        'desc' : todo['desc']
    }

    all_todo.append(new_todo)
    return  new_todo

#to give input without interfaace fast api gives us auto docs "/docs"

@api.put('/todos/{tid}')
def update_todo(tid :int , updated_todo :dict):
    for todo in all_todo:
        if todo['tid'] == tid:
            todo['name']=updated_todo['name']
            todo['desc'] = updated_todo['desc']
            return todo
    return "error not found"


@api.delete("/todo/{tid}")
def delete_todo (tid : int):
    for index, todo in enumerate (all_todo):
        if todo['tid']==tid:
            deleted_todo =all_todo.pop(index)
            return deleted_todo
    return "Eror not found"








