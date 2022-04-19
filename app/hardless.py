import uuid
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.forms import UserLoginForm, UserCreateForm
from app.models import connect_db, User, Authtoken
from app.utils import get_password_hash


router = APIRouter()

@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
    user = database.query(User).filter(User.email == user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {'error': 'email/passowrd invalid'}
    auth_token = Authtoken(token=str(uuid.uuid4()), user_id=user.id)
    database.add(auth_token)
    database.commit()
    return {'status': 'ok'}

@router.post('/signup', name='user:create')
def create_user(user: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    exist_user = database.query(User.id).filter(User.email == user.email).one_or_none()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already exist')
    new_user = User(
        email=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
    )
    database.add(new_user)
    database.commit()
    return {'new_user': new_user.id}