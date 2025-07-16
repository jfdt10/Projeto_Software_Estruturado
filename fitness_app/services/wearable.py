"""
Serviço de Treino para o aplicativo de fitness.
Este módulo fornece funcionalidades para wearables, registrar dados manuais, gerar simulações de dados de um wearable, listar e deletar dados.
"""

from core.models import DadoWearable
from core.database import inserir_registro, obter_registros, deletar_registro
import random
from datetime import datetime

class ServicoWearable:
    def registrar_dado_manual(self, usuario_email, tipo, valor, data=None):
        dado = DadoWearable(
            usuario_email=usuario_email,
            data=data or datetime.now().isoformat(),
            tipo=tipo,  
            valor=valor
        )
        return inserir_registro('wearable', dado.to_dict())

    def gerar_dado_aleatorio(self, usuario_email, tipo, data=None):
        if tipo == "passos":
            valor = random.randint(3000, 15000)
        elif tipo == "batimentos":
            valor = random.randint(60, 180)
        elif tipo == "sono":
            valor = round(random.uniform(5, 9), 1)  
        else:
            valor = random.randint(1, 100)
        return self.registrar_dado_manual(usuario_email, tipo, valor, data)

    def listar_dados_usuario(self, usuario_email):
        return [
            DadoWearable.from_dict(dado)
            for dado in obter_registros('wearable')
            if dado.get('usuario_email') == usuario_email
        ]

    def deletar_dado(self, doc_id):
        return deletar_registro('wearable', doc_id)