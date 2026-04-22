import requests

def verificar_seguranca():
    url = "https://www.google.com" # Você pode trocar pelo site que quiser testar
    print(f"Verificando {url}...")
    
    try:
        r = requests.get(url)
        headers = r.headers
        
        # Headers que protegem contra hackers
        seguros = ["Strict-Transport-Security", "X-Content-Type-Options", "X-Frame-Options"]
        
        for item in seguros:
            if item in headers:
                print(f"✅ {item} está configurado!")
            else:
                print(f"❌ ALERTA: {item} NÃO encontrado!")
                
    except:
        print("Erro ao acessar o site.")

if __name__ == "__main__":
    verificar_seguranca()