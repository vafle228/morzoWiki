from django.shortcuts import render
from .forms import MorzoForm

def getMorzo(request):
	if request.method == 'POST':
		form = MorzoForm(request.POST)
		if form.is_valid:
			form = MorzoForm()
			codeWord = stringToMorzo(request.POST.get('string'))
			return render(request, 'main/index.html', {'data': codeWord, 'form': form})
	form = MorzoForm()
	return render(request, 'main/index.html', {'form': form})

def stringToMorzo(string):
	
	morzoCodeDict = {
		'а': '.-',
		'б': '..',
		'в': '.--',
		'г': '--.',
		'д': '..',
		'е': '.',
		'ж': '...-',
		'з': '--..',
		'и': '..',
		'й': '.---',
		'к': '-.-',
		'л': '.-..',
		'м': '--',
		'н': '-.',
		'о': '---',
		'п': '.--.',
		'р': '.-.',
		'с': '...',
		'т': '-',
		'у': '..-',
		'ф': '..-.',
		'х': '....',
		'ц': '-.-.',
		'ч': '---.',
		'ш': '----',
		'щ': '--.-',
		'ъ': '-..-',
		'ы': '-.--',
		'ь': '-..-',
		'э': '..-..',
		'ю': '..--',
		'я': '.-.-',
		' ': '.-.-.'
	}

	morzoDecodeDict = {
		'.-': 'а', 
		'..': 'б',
		'.--': 'в',
		'--.': 'г',
		'..': 'д',
		'.': 'е',
		'...-': 'ж',
		'--..': 'з',
		'..': 'и',
		'.---': 'й',
		'-.-': 'к',
		'.-..': 'л',
		'--': 'м',
		'-.': 'н',
		'---': 'о',
		'.--.': 'п',
		'.-.': 'р',
		'...': 'с',
		'-': 'т',
		'..-': 'у',
		'..-.': 'ф',
		'....': 'х',
		'-.-.': 'ц',
		'---.': 'ч',
		'----': 'ш',
		'--.-': 'щ',
		'-..-': 'ъ',
		'-.--': 'ы',
		'-..-': 'ь',
		'..-..': 'э',
		'..--': 'ю',
		'.-.-': 'я',
		'.-.-.': ' '
	}

	if string.replace('-', '').replace('.', '').replace(' ', '').replace('*', ''):
		string = string.lower()
		codeWord = ''
		for i in string:
			codeWord += morzoCodeDict.get(i) + ' '
	else:
		string = string.replace('*', '.').split(' ')
		codeWord = ''
		for i in string:
			codeWord += morzoDecodeDict.get(i)

	return codeWord

