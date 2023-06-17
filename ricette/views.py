from django.shortcuts import render, redirect
from .models import Ricetta, Utente

# Create your views here.
def ricette(request):
    ricette = Ricetta.objects.all()
    return render(request, "ricette/ricette.html", {'ricette': ricette})

def primi(request):
    ricette = Ricetta.objects.all()
    return render(request, "ricette/primi.html",  {'ricette': ricette})

def secondi(request):
    ricette = Ricetta.objects.all()
    return render(request, "ricette/secondi.html",  {'ricette': ricette})

def contorni(request):
    ricette = Ricetta.objects.all()
    return render(request, "ricette/contorni.html",  {'ricette': ricette})

def dolci(request):
    ricette = Ricetta.objects.all()
    return render(request, "ricette/dolci.html",  {'ricette': ricette})

def search(request):
    query_dict = request.GET
    query = query_dict.get("query")
    ricetta=None
    for r in Ricetta.objects.all():
        if r.nome == query:
            ricetta = r
    context = {
        "object": ricetta
    }
    return render(request, 'ricette/search.html', context=context)

def accedi(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pw = request.POST.get("pw")
        user = None
        for u in Utente.objects.all():
            if(u.email == email and u.password == pw):
                user = u
        if user is None:
            context = {
                "error": "Email o Password errate, riprova"
            }
            return render(request, 'ricette/accedi.html', context)
        request.session['user'] = user.nickname
        return redirect('accesso')
    return render(request, 'ricette/accedi.html', {})

def registrati(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        email = request.POST.get("email")
        pw = request.POST.get("pw")
        for u in Utente.objects.all():
            if (u.email == email or u.nickname == nickname):
                context = {
                    "error": "Utente già registrato, esegui accesso"
                }
                return render(request, 'ricette/registrati.html', context)
        user_object = Utente.objects.create(nickname=nickname, email=email, password=pw)
        return redirect('/home/accedi')
    return render(request, 'ricette/registrati.html', {})

def accesso(request):
    ricette = Ricetta.objects.all()
    if request.method == "POST":
        ricetta = request.POST.get("ricetta_nome")
        utenti = Utente.objects.all()
        user = request.session['user']
        for u in utenti:
            if u.nickname == user:
                utente = u
        for r in ricette:
            if r.nome == ricetta:
                ri = r
        utente.preferiti.add(ri)
        return redirect('preferiti')
    return render(request, 'ricette/accesso.html', {'ricette': ricette})


def primi_a(request):
    ricette = Ricetta.objects.all()
    if request.method == "POST":
        ricetta = request.POST.get("ricetta_nome")
        utenti = Utente.objects.all()
        user = request.session['user']
        for u in utenti:
            if u.nickname == user:
                utente = u
        for r in ricette:
            if r.nome == ricetta:
                ri = r
        utente.preferiti.add(ri)
        return redirect('preferiti')
    return render(request, 'ricette/primi_a.html', {'ricette': ricette})

def secondi_a(request):
    ricette = Ricetta.objects.all()
    if request.method == "POST":
        ricetta = request.POST.get("ricetta_nome")
        utenti = Utente.objects.all()
        user = request.session['user']
        for u in utenti:
            if u.nickname == user:
                utente = u
        for r in ricette:
            if r.nome == ricetta:
                ri = r
        utente.preferiti.add(ri)
        return redirect('preferiti')
    return render(request, 'ricette/secondi_a.html', {'ricette': ricette})

def contorni_a(request):
    ricette = Ricetta.objects.all()
    if request.method == "POST":
        ricetta = request.POST.get("ricetta_nome")
        utenti = Utente.objects.all()
        user = request.session['user']
        for u in utenti:
            if u.nickname == user:
                utente = u
        for r in ricette:
            if r.nome == ricetta:
                ri = r
        utente.preferiti.add(ri)
        return redirect('preferiti')
    return render(request, 'ricette/contorni_a.html', {'ricette': ricette})

def dolci_a(request):
    ricette = Ricetta.objects.all()
    if request.method == "POST":
        ricetta = request.POST.get("ricetta_nome")
        utenti = Utente.objects.all()
        user = request.session['user']
        for u in utenti:
            if u.nickname == user:
                utente = u
        for r in ricette:
            if r.nome == ricetta:
                ri = r
        utente.preferiti.add(ri)
        return redirect('preferiti')
    return render(request, 'ricette/dolci_a.html', {'ricette': ricette})

def search_a(request):
    ricette = Ricetta.objects.all()
    if request.method == "POST":
        ricetta = request.POST.get("ricetta_nome")
        utenti = Utente.objects.all()
        user = request.session['user']
        for u in utenti:
            if u.nickname == user:
                utente = u
        for r in ricette:
            if r.nome == ricetta:
                ri = r
        utente.preferiti.add(ri)
        return redirect('preferiti')
    query_dict = request.GET
    query = query_dict.get("query")
    ricetta=None
    for r in Ricetta.objects.all():
        if r.nome == query:
            ricetta = r
    context = {
        "object": ricetta
    }
    return render(request, 'ricette/search_a.html', context=context)

def preferiti(request):
    utenti = Utente.objects.all()
    user = request.session['user']
    for u in utenti:
        if u.nickname == user:
            utente = u
    return render(request, 'ricette/preferiti.html', {'utente': utente})

def aggiungi(request):
    if request.method == "POST":
        categoria = request.POST.get("Categoria")
        nome = request.POST.get("Nome")
        descrizione = request.POST.get("Descrizione")
        ingredienti = request.POST.get("Ingredienti")
        tempo = request.POST.get("Tempo")
        difficoltà = request.POST.get("Difficoltà")
        immagine = request.FILES.get("Immagine")
        for r in Ricetta.objects.all():
            if (r.nome == nome):
                context = {
                    "error": "Ricetta già presente"
                }
                return render(request, 'ricette/aggiungi.html', context)
        ricetta_object = Ricetta.objects.create(immagine=immagine, nome=nome, ingredienti=ingredienti, difficoltà=difficoltà, tempo=tempo, descrizione=descrizione, categoria=categoria)
        return redirect('/home/accesso')
    return render(request, 'ricette/aggiungi.html', {})
