class Usuario:
    def __init__(
        self,
        nome,
        email,
        senha,
        genero,
        idade,
        peso,
        altura,
        nivel_atividade,
        objetivo,
        nivel_experiencia,
        frequencia_treino=None,
        preferencia_treino=None,
        restricoes_treino=None,
        dias_treino=None,
        tipo_dieta=None,
        dados_wearable=None,
        perfil_completo=False,
        criado_em=None,
    ):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.genero = genero
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.nivel_atividade = nivel_atividade
        self.objetivo = objetivo
        self.nivel_experiencia = nivel_experiencia
        self.frequencia_treino = frequencia_treino
        self.preferencia_treino = preferencia_treino
        self.restricoes_treino = restricoes_treino
        self.dias_treino = dias_treino
        self.tipo_dieta = tipo_dieta
        self.dados_wearable = dados_wearable
        self.perfil_completo = perfil_completo
        self.criado_em = criado_em

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Usuario(
            nome=data.get("nome"),
            email=data.get("email"),
            senha=data.get("senha"),
            genero=data.get("genero"),
            idade=data.get("idade"),
            peso=data.get("peso"),
            altura=data.get("altura"),
            nivel_atividade=data.get("nivel_atividade"),
            objetivo=data.get("objetivo"),
            nivel_experiencia=data.get("nivel_experiencia"),
            frequencia_treino=data.get("frequencia_treino"),
            preferencia_treino=data.get("preferencia_treino"),
            restricoes_treino=data.get("restricoes_treino"),
            dias_treino=data.get("dias_treino"),
            tipo_dieta=data.get("tipo_dieta"),
            dados_wearable=data.get("dados_wearable"),
            perfil_completo=data.get("perfil_completo", False),
            criado_em=data.get("criado_em")
        )

class PlanoTreino:
    def __init__(self, usuario_email, nome, exercicios, objetivo, nivel, criado_em=None):
        self.usuario_email = usuario_email
        self.nome = nome
        self.exercicios = exercicios
        self.objetivo = objetivo
        self.nivel = nivel
        self.criado_em = criado_em

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return PlanoTreino(
            usuario_email=data.get("usuario_email"),
            nome=data.get("nome"),
            exercicios=data.get("exercicios"),
            objetivo=data.get("objetivo"),
            nivel=data.get("nivel"),
            criado_em=data.get("criado_em")
        )

class Atividade:
    def __init__(self, usuario_email, tipo, data, duracao, calorias, passos=None):
        self.usuario_email = usuario_email
        self.tipo = tipo
        self.data = data
        self.duracao = duracao
        self.calorias = calorias
        self.passos = passos

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Atividade(
            usuario_email=data.get("usuario_email"),
            tipo=data.get("tipo"),
            data=data.get("data"),
            duracao=data.get("duracao"),
            calorias=data.get("calorias"),
            passos=data.get("passos")
        )

class RegistroNutricional:
    def __init__(self, usuario_email, data, refeicoes, calorias, macros):
        self.usuario_email = usuario_email
        self.data = data
        self.refeicoes = refeicoes
        self.calorias = calorias
        self.macros = macros

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return RegistroNutricional(
            usuario_email=data.get("usuario_email"),
            data=data.get("data"),
            refeicoes=data.get("refeicoes"),
            calorias=data.get("calorias"),
            macros=data.get("macros")
        )

class Meta:
    def __init__(self, usuario_email, tipo, valor, data_inicio, data_fim, atingida=False):
        self.usuario_email = usuario_email
        self.tipo = tipo
        self.valor = valor
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.atingida = atingida

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Meta(
            usuario_email=data.get("usuario_email"),
            tipo=data.get("tipo"),
            valor=data.get("valor"),
            data_inicio=data.get("data_inicio"),
            data_fim=data.get("data_fim"),
            atingida=data.get("atingida", False)
        )

class DadoWearable:
    def __init__(self, usuario_email, data, tipo, valor):
        self.usuario_email = usuario_email
        self.data = data
        self.tipo = tipo
        self.valor = valor

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return DadoWearable(
            usuario_email=data.get("usuario_email"),
            data=data.get("data"),
            tipo=data.get("tipo"),
            valor=data.get("valor")
        )

class Desafio:
    def __init__(self, nome, descricao, data_inicio, data_fim, participantes=None):
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.participantes = participantes or []

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Desafio(
            nome=data.get("nome"),
            descricao=data.get("descricao"),
            data_inicio=data.get("data_inicio"),
            data_fim=data.get("data_fim"),
            participantes=data.get("participantes", [])
        )

class Video:
    def __init__(self, titulo, url, categoria):
        self.titulo = titulo
        self.url = url
        self.categoria = categoria

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Video(
            titulo=data.get("titulo"),
            url=data.get("url"),
            categoria=data.get("categoria")
        )

class Recomendacao:
    def __init__(self, usuario_email, tipo, conteudo, data):
        self.usuario_email = usuario_email
        self.tipo = tipo
        self.conteudo = conteudo
        self.data = data

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Recomendacao(
            usuario_email=data.get("usuario_email"),
            tipo=data.get("tipo"),
            conteudo=data.get("conteudo"),
            data=data.get("data")
        )

class Feedback:
    def __init__(self, usuario_email, texto, nota, data):
        self.usuario_email = usuario_email
        self.texto = texto
        self.nota = nota
        self.data = data

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Feedback(
            usuario_email=data.get("usuario_email"),
            texto=data.get("texto"),
            nota=data.get("nota"),
            data=data.get("data")
        )

class PostForum:
    def __init__(self, usuario_email, titulo, mensagem, data):
        self.usuario_email = usuario_email
        self.titulo = titulo
        self.mensagem = mensagem
        self.data = data

    def to_dict(self):
        return self.__dict__

    @staticmethod # decorator para não modificar os atributos da instância constructor
    def from_dict(data):
        return PostForum(
            usuario_email=data.get("usuario_email"),
            titulo=data.get("titulo"),
            mensagem=data.get("mensagem"),
            data=data.get("data")
        )