# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.phrase_all import PhraseAll
from app.models.phrase_organic import PhraseOrganic
from app.models.phrase_related import PhraseRelated
from app.models.phrase_fullsearch import PhraseFullSearch
from app.models.phrase_kdi import PhraseKdi
from app.models.phrase_adwords import PhraseAdwords
from app.models.phrase_adwords_historical import PhraseAdwordsHistorical
from app.models.phrase_this import PhraseThis
from app.models.domain_domains import DomainDomains
from app.models.domain_organic import DomainOrganic
from app.models.backlinks_overview import BacklinksOverview
from app.models.url_organic import UrlOrganic
from app.models.log import Log