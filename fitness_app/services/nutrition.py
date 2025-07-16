"""
Serviço de Treino para o aplicativo de fitness.
Este Módulo fornece funcionalidades para registrar atividades, listar atividades do usuário, atualizar e deletar atividades.
"""

from core.models import RegistroNutricional
from core.database import inserir_registro, obter_registros, atualizar_registro, deletar_registro
import json
import os

class ServicoNutricional:
    def registrar_refeicao(self, registro: RegistroNutricional):
        return inserir_registro('nutricao', registro.to_dict())

    def listar_registros_usuario(self, usuario_email):
        return [
            RegistroNutricional.from_dict(dado)
            for dado in obter_registros('nutricao')
            if dado.get('usuario_email') == usuario_email
        ]

    def atualizar_registro(self, doc_id, novos_dados: dict):
        return atualizar_registro('nutricao', doc_id, novos_dados)

    def deletar_registro(self, doc_id):
        return deletar_registro('nutricao', doc_id)

    def buscar_alimento(self, nome_alimento):
        caminho = os.path.join("data", "food_database.json")
        with open(caminho, encoding="utf-8") as f:
            alimentos = json.load(f)
        for alimento in alimentos:
            if alimento["alimento"].lower() == nome_alimento.lower():
                return alimento
        return None

    def analisar_consumo(self, usuario_email):
        registros = self.listar_registros_usuario(usuario_email)
        total_calorias = sum(r.calorias for r in registros)
        total_proteina = sum(r.macros.get("proteina", 0) for r in registros)
        total_gordura = sum(r.macros.get("gordura", 0) for r in registros)
        total_carbo = sum(r.macros.get("carboidrato", 0) for r in registros)
        return {
            "calorias": total_calorias,
            "proteina": total_proteina,
            "gordura": total_gordura,
            "carboidrato": total_carbo
        }