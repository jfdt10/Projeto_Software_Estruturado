"""
Serviço de Treino para o aplicativo de fitness.
Este módulo fornece funcionalidades para recomendar treinos, criar planos personalizados,
"""

from core.models import PlanoTreino
from core.database import inserir_registro, obter_registros, atualizar_registro, deletar_registro
import json
import os

class ServicoTreino:
    def __init__(self, caminho_workouts="data/workouts.json"):
        self.caminho_workouts = caminho_workouts

    def recomendar_treinos(self, usuario):
        """
        Sugere treinos prontos do workouts.json baseados no nível e objetivo do usuário.
        """
        with open(self.caminho_workouts, encoding="utf-8") as f:
            treinos = json.load(f)
        recomendados = [
            t for t in treinos
            if t["nivel"] == usuario.nivel_experiencia and t["objetivo"] == usuario.objetivo
        ]
        return recomendados

    def criar_plano_personalizado(self, usuario_email, nome, exercicios, objetivo, nivel):
        plano = PlanoTreino(
            usuario_email=usuario_email,
            nome=nome,
            exercicios=exercicios,
            objetivo=objetivo,
            nivel=nivel
        )
        return inserir_registro('planos_treino', plano.to_dict())

    def listar_planos_usuario(self, usuario_email):
        return [
            PlanoTreino.from_dict(dado)
            for dado in obter_registros('planos_treino')
            if dado.get('usuario_email') == usuario_email
        ]

    def atualizar_plano(self, doc_id, novos_dados: dict):
        return atualizar_registro('planos_treino', doc_id, novos_dados)

    def deletar_plano(self, doc_id):
        return deletar_registro('planos_treino', doc_id)