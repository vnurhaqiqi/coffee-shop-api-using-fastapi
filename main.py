from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
coffee_dict_db = [
    {
        'id': 1,
        'name': "AMERICANO",
        'price': 15000

    },
    {
        'id': 2,
        'name': "Ice Coffee",
        'price': 18000
    },
    {
        'id': 3,
        'name': "Ice Latte",
        'price': 18000
    }
]


class Coffee(BaseModel):
    name: str
    price: int


@app.get('/')
async def index():
    return "Hello! Welcome to Coffee Shop."


@app.get('/coffee-menu')
async def get_all_coffees():
    return coffee_dict_db


@app.get('/coffee/{id}')
async def get_coffee(id):
    for coffee in coffee_dict_db:
        if (coffee['id'] == int(id)):
            return coffee

    return {'error': "Coffee with id {id} not found.".format(id=id)}


@app.post('/add-coffee')
async def add_coffee(coffee: Coffee):
    new_coffee = coffee.dict()

    new_coffee['id'] = coffee_dict_db[-1]['id'] + 1
    coffee_dict_db.append(new_coffee)

    return {'success': "{name} has been added to menu".format(name=new_coffee['name'])}


@app.delete('/delete-coffee/{id}')
async def delete_coffee(id):
    for i in range(len(coffee_dict_db)):
        if coffee_dict_db[i]['id'] == int(id):
            del coffee_dict_db[i]

            return {'success': "{name} has been deleted from menu".format(name=coffee_dict_db[i]['name'])}

    return {'error': "Coffee with id {id} not found.".format(id=id)}
