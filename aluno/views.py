from django.shortcuts import render, redirect
from .models import Pessoa


# Página inicial
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})


# Salvar novo aluno
def salvar(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        cep = request.POST.get("cep")
        rua = request.POST.get("rua")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")

        Pessoa.objects.create(
            nome=nome,
            idade=idade,
            email=email,
            cpf=cpf,
            cep=cep,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            estado=estado
        )

    return redirect(home)


# Abrir página de edição
def editar(request, id):

    pessoa = Pessoa.objects.get(id=id)

    return render(request, "update.html", {"pessoa": pessoa})


# Atualizar aluno
def update(request, id):

    if request.method == "POST":

        pessoa = Pessoa.objects.get(id=id)

        pessoa.nome = request.POST.get("nome")
        pessoa.idade = request.POST.get("idade")
        pessoa.email = request.POST.get("email")
        pessoa.cpf = request.POST.get("cpf")
        pessoa.cep = request.POST.get("cep")
        pessoa.rua = request.POST.get("rua")
        pessoa.bairro = request.POST.get("bairro")
        pessoa.cidade = request.POST.get("cidade")
        pessoa.estado = request.POST.get("estado")

        pessoa.save()

    return redirect(home)


# Deletar aluno
def delete(request, id):

    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()

    return redirect(home)

