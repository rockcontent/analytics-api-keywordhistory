from .crud_item import item
from .crud_user import user
from .crud_phrase_all import phrase_all
from .crud_phrase_organic import phrase_organic
from .crud_phrase_this import phrase_this

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
