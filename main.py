from fastapi import FastAPI

app = FastAPI()
persons = [{'id': 1, 'ad': 'Seyma', 'soyad': 'Sarıgil', 'meslek': 'Gelistirici', 'memleket': 'Hatay'},
           {'id': 2, 'ad': 'Alp', 'soyad': 'Kara', 'meslek': 'Müzisyen', 'memleket': 'İstanbul'}]


@app.get("/")
def get_all_persons():
    return persons


@app.post("/add_person")
def add_person(ad, soyad, meslek, memleket):
    id_ = persons[-1]['id'] + 1
    person = {'id': id_, 'ad': ad, 'soyad': soyad, 'meslek': meslek, 'memleket': memleket}
    persons.append(person)
    return {"item": persons}


@app.get("/get_person/{person_id}")
def get_specific_person(person_id: int):
    person = [i for i in persons if i['id'] == person_id]
    return {"item": persons}


@app.put("/update_person/{person_id}")
def update_name_person(person_id: int, new_person_name: str):
    person = [i for i in persons if i['id'] == person_id]
    person[0]['ad'] = new_person_name
    return {"item": persons}


@app.delete("/delete_person/{person_id}")
def delete_person(person_id: int):
    person = [i for i in persons if i['id'] == person_id]
    persons.remove(person[0])
    return {"item": persons}
