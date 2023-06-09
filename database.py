import sqlalchemy
from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://qzxvphrula8xbmqboee2:pscale_pw_dRRy5yNTSU1mIRLopeoy5TkNED1Uxj4Az6fKEcHsUAh@aws.connect.psdb.cloud/testcareers?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args = {
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

print(sqlalchemy.__version__)
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result.all():", type(result_all))
  first_result = result_all[0]
  print("type(first_result):", type(first_result))
  first_result_dict = dict(result_all[0]._asdict())
  print("type(first_result_dict):", type(first_result_dict))
  print(first_result_dict)