from django.db import models


class Diligencia():
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_realizacao = models.DateField(null=False, blank=False)
    mandado = models.FileField(upload_to='mandados/', null=True, blank=True)
    relatorio = models.FileField(upload_to='relatorios/', null=True, blank=True)
    dinheiro_apreendido = models.DecimalField(max_digits=15, decimal_places=2)
    obs = models.TextField()
    endereco = models.ForeignKey(Endereco, blank=False, null=False, on_delete=models.CASCADE)
    pessoa = models.ManyToManyField(Pessoa, blank=True)

    def __str__(self):
        return self.nome