"""
Serviço de Treino para o aplicativo de fitness.
Este Módulo fornece funcionalidades para registrar atividades, listar atividades do usuário, atualizar e deletar atividades.
"""

from core.models import Atividade
from core.database import inserir_registro, obter_registros, atualizar_registro, deletar_registro

class ServicoAtividade:
    def registrar_atividade(self, atividade: Atividade):
        return inserir_registro('atividades', atividade.to_dict())

    def listar_atividades_usuario(self, usuario_email):
        return [
            Atividade.from_dict(dado)
            for dado in obter_registros('atividades')
            if dado.get('usuario_email') == usuario_email
        ]

    def atualizar_atividade(self, doc_id, novos_dados: dict):
        return atualizar_registro('atividades', doc_id, novos_dados)

    def deletar_atividade(self, doc_id):
        return deletar_registro('atividades', doc_id)