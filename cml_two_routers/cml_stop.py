from virl2_client import ClientLibrary

url = os.environ.get("CML_URL")
user = os.environ.get('CML_USER')
password = os.environ.get("CMLPASSWORD")

client = ClientLibrary(url, user, password, ssl_verify=False)
client.await_for_lld_connected()
labs = client.all_labs()
for lab in labs:
    lab.stop()