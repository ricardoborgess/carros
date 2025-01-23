from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields =  '__all__' 
    
    # Função para validação de campo. Tem que sempre começar com clean para o django entender. 
    def clean_value(self): 
        value = self.cleaned_data.get('value')  # Capturando o valor
        if value < 20000:
            self.add_error('value', 'Não é possível cadastrar carros abaixo do valor de R$20.000.')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastradar carros fabricados antes de 1975.')
        return factory_year
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            self.add_error('photo', 'Não é possível cadastrar carro sem foto.')
        return photo