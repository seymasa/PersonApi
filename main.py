from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()
persons = [{'id': 1, 'ad': 'Seyma', 'soyad': 'Sarıgil', 'meslek': 'Gelistirici', 'memleket': 'Hatay'},
           {'id': 2, 'ad': 'Alp', 'soyad': 'Kara', 'meslek': 'Müzisyen', 'memleket': 'İstanbul'}]


class Person(BaseModel):
    id: Optional[int] = None
    ad: str
    soyad: str
    meslek: str
    memleket: str

    if __name__ == "__main__":
        id = persons[-1]['id'] + 1


@app.get("/")
def get_all_persons():
    return persons


@app.post("/add_person/")
def add_person(person: Person): #ad, soyad, meslek, memleket
    person_dict = person.dict()
    person_dict['id'] = persons[-1]['id'] + 1
    persons.append(dict(person_dict))
    return persons


@app.get("/get_person/{person_id}")
def get_specific_person(person_id: int):
    person = [i for i in persons if i['id'] == person_id]
    return person


@app.put("/update_person/{person_id}")
def update_name_person(person_id: int, new_person_name: str):
    person = [i for i in persons if i['id'] == person_id]
    person[0]['ad'] = new_person_name
    return persons


@app.delete("/delete_person/{person_id}")
def delete_person(person_id: int):
    person = [i for i in persons if i['id'] == person_id]
    persons.remove(person[0])
    return person
