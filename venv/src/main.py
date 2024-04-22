import warframemarket
from secrets import secrets


wfm = warframemarket.api(secrets.get()["jwt"])

#wfm.setUser(secrets.get()["email"], secrets.get()["password"], "pc")
wfm.login()
