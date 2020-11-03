import gcsa
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from Bot.core.bot import *

logger = logging.getLogger(__name__)


class Calender(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner())
    async def cal(self, ctx):
        try:
            calendar = GoogleCalendar("rowanthen@gmail.com",
                                      '../../Configuration/googleCalendar.json')
            for event in calendar:
                print(event)
        except:
            logging.exception("Got exception on main handler")
            raise


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(Calender(client))
    logging.info("StartUp loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("StartUp unloaded!")
