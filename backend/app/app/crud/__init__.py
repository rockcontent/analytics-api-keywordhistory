#from .crud_item import item
from .crud_user import user
from .crud_phrase_all import phrase_all
from .crud_phrase_organic import phrase_organic
from .crud_phrase_this import phrase_this
from .crud_phrase_adwords import phrase_adwords
from .crud_phrase_fullsearch import phrase_fullsearch
from .crud_phrase_related import phrase_related
from .crud_phrase_adwords_historical import phrase_adwords_historical
from .crud_phrase_kdi import phrase_kdi
from .crud_domain_domains import domain_domains
from .crud_domain_organic import domain_organic
from .crud_backlinks_overview import backlinks_overview
from .crud_url_organic import url_organic

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
