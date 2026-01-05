from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
app = FastAPI()



contacts=[
  {
    'id':1,
    'name':'Nandhini',
    'number':'8977166762'
  },
  {
    'id':2,
    'name':'sagarika',
    'number':'8374728187'
  }
]

@app.get('/contacts')
def get_all_contacts():
    return  contacts

@app.get('/contact')
def get_contact(contact_id):
    for c in contacts:
        if c['id'] == int(contact_id):
            return c
    return "contact is not listed"

@app.post('/add/contacts')
async def add_contact(request: Request):
    data =await request.json()
    contacts.append(data)
    return contacts

@app.put('/update/contacts')
async def update_contact(request: Request):
    data = await request.json()
    for c in contacts:
        if c['id']== data['id']:
            c.update(data)
            return contacts
    return "existing contact id is not found"


@app.delete('/contact/{contact_id}')
def delete_contact(contact_id):
    for c in contacts:
        if c['id']== int(contact_id):
            contacts.remove(c)
            return contacts
        return "No such contact found"