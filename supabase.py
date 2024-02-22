
import supabase

supabase_url = "https://meyejehzcuycclfcjzyp.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1leWVqZWh6Y3V5Y2NsZmNqenlwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDc4Mjg4NzEsImV4cCI6MjAyMzQwNDg3MX0.hhfxkn13HW0016L_1mHSLr4ZCqISRaKF8dD09Ny3fL8"
client = supabase.create_client(supabase_url, supabase_key)

# SELECT query
result = client.table("person").select("*").execute()
print(result["data"])
