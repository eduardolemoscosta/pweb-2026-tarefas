from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluída', 'Concluída'),
    ]
    
    nome = models.CharField(max_length=150, verbose_name="Nome da Tarefa")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente', verbose_name="Status")
    prazo = models.DateField(verbose_name="Prazo de Entrega")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['prazo']

    def __str__(self):
        return self.nome


