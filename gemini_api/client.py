from decouple import config
import google.generativeai as genai 

# Pegando a chave do arquivo .env
api_key = config('API_KEY')

# Configurando a API corretamente
genai.configure(api_key=api_key)
def car_gemini_ai(model, brand, year): 
    message = ''' Elaborar um resumo sobre o carro {} da marca {} do ano {} com espeficações tecnicas com 200 caracteres. ''' 
    message = message.format(model, brand, year)
    model = genai.GenerativeModel("gemini-1.5-flash") 
    response = model.generate_content( message, generation_config = genai.GenerationConfig( max_output_tokens=300, ) ) 
    return response.text 
