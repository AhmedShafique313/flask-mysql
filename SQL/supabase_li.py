#  pip install supabase python-dotenv
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get('SUPABASE_KEY')
supabase = create_client(url, key)

# for selecting data 
# means reading data 
data = supabase.table("Signs").select("*").execute()
print(data)
member1 = "Chery"
data = supabase.table("Signs").insert({"name":"John"}).execute()
print(data)
data = supabase.table("Signs").insert({"name":member1}).execute()
print(data)

data = supabase.table("Signs").delete().eq("id", 3).execute()
print(data)