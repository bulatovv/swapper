from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from secrets import token_urlsafe
from models import User, Item, Trade, RegistrationConfirm
from schemas import UserRegistration

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth-tokens")

@router.post("/registration-confirms")
async def register_user(user_registration: UserRegistration):
    token = token_urlsafe(32)
    
    user = await User.create(
        email=user_registration.username,
        password_hash=user_registration.password,
        name=user_registration.name
    )


    confirm = await RegistrationConfirm.create(
        token = token_urlsafe(32),
        user=user
    )

    print(confirm.token)

    return f"Registration confirmation sent"



@router.post("/users")
def confirm_registration(token: str):
    pass



@router.post("/auth-tokens")
def login_user(username: str, password: str):
    pass


@router.get("/items/")
def index_items():
    pass

@router.get("/items/{item_id}")
def show_item(item_id: int):
    pass

@router.post("/items/")

@router.get("/trades/")
def index_trades():
    pass


