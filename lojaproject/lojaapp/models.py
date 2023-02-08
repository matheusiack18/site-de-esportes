from django.db import models
from django.contrib.auth.models import User

# on_delete=models.CASCADE (valor default): Quando um registro é excluído do banco, todos os registros associados na tabela relacionada são excluídos também.

# on_delete=models.PROTECT: Se houver qualquer tentativa de excluir um registro de uma tabela e este possuir registros associados em outra tabela, a operação não será realizada, levantando uma exceção IntegrityError.

# on_delete=models.SET_NULL: Se um registro for excluído, os campos que apontavam para ele nas tabelas relacionadas serão preenchidos com o valor NULL (o equivalente, em bancos de dados relacionais, ao None do Python). Essa opção não costuma ser usada com muita frequência, porque gera registros órfãos1 no banco de dados e, além disso, só funciona se o campo possuir propriedade null=True.

# on_delete=models.SET_DEFAULT: Se um registro for excluído, os campos que apontavam para ele nas tabelas relacionadas serão preenchidos com o seu valor default. Essa opção só funciona se o campo tiver um valor definido para a propriedade default.

# on_delete=models.SET: Se um registro for excluído, os campos que apontavam para ele nas tabelas relacionadas serão preenchidos por meio de uma função, passada como parâmetro. Por exemplo: on_delete=models.SET(retorna_cliente_vazio) instruirá o framework a chamar o método retorna_retorna_cliente_vazio() para atribuir um valor ao campo. Em geral, essa estratégia é usada quando seu sistema não exclui nenhum 
#registro, apenas marca-os com um valor especial que significa “excluído” para o projeto. Você encontrará esse tipo de código em aplicações que lidam com dados sensíveis e não podem perder nenhum trecho de informação, mesmo que isso signifique investir em infraestrutura para armazenar anos de dados que não serão mais acessados.

# on_delete=models.DO_NOTHING: Não faz nada para garantir a integridade dos dados se um registro for excluído. É considerada uma má prática devido ao seu potencial de gerar registros órfãos. Além disso, se o mecanismo do seu banco de dados implementar algum controle de registros órfãos, poderão ocorrer erros originados no SGBD.

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    nome_completo = models.CharField(max_length=200)
    image = models.ImageField(upload_to="admins")
    tel = models.CharField(max_length=20)

    def __str__(self) :
        return self.user.username
    
class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    nome_completo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200,null=True,blank=True)
    data_on = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.nome_completo

class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) :
        return self.titulo

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="produtos")
    preco_mercado = models.PositiveIntegerField()
    venda = models.PositiveIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300,null=True,blank=True)
    return_devolucao = models.CharField(max_length=300,null=True,blank=True)
    visualizacao = models.PositiveIntegerField(default=0)

    def __str__(self) :
        return self.titulo
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True,blank=True) 
    total = models.PositiveIntegerField(default=0)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self) :
        return "Carro" + str(self.id)
        
class CarroProduto(models.Model):
    carro = models.ForeignKey(Carro,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self) :
        return "Carro" + str(self.carro.id) + "CarroProduto:" + str(self.id)

PEDIDO_STATUS =(
    ("Pedido Recebido","Pedido Recebido"),
    ("Pedido Processando","Pedido Processando"),
    ("Pedido a Caminho","Pedido a Caminho"),
    ("Pedido Completado","Pedido Completado"),
    ("Pedido Cancelado","Pedido Cancelado"),
)

METHOD = (
    ("Dinheiro na Entrega","Dinheiro na Entrega"),
    ("Khalti","Khalti"),

)

class Pedido_order(models.Model):
    carro = models.OneToOneField(Carro,on_delete=models.CASCADE)
    ordernando_por = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(null=True,blank=True)
    endereco_envio = models.CharField(max_length=200)
    subtotal = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    pedido_status = models.CharField(max_length=50,choices=PEDIDO_STATUS)
    criado_em = models.DateTimeField(auto_now_add=True)
    pagamento_method = models.CharField(max_length=20, choices=METHOD, default="Dinheiro na Entrega")
    pagamento_completo = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self) :
        return "Pedido_order:" + str(self.id)

    
