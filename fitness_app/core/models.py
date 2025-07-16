"""
Modelos para o aplicativo de fitness.
Inclui modelos para usuários, exercícios, treinos e outros componentes essenciais.
"""

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


def usuario_from_dict(data):
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
