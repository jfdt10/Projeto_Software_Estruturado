from core.auth import ServicoAutenticacao
from services.workout import ServicoTreino
from services.activity import ServicoAtividade
from services.nutrition import ServicoNutricional
from services.goal import ServicoMeta
from services.wearable import ServicoWearable
from services.social import ServicoSocial


try:
    from services.video import ServicoVideo
except ImportError:
    ServicoVideo = None

try:
    from services.recommendation import ServicoRecomendacao
except ImportError:
    ServicoRecomendacao = None

try:
    from services.feedback import ServicoFeedback
except ImportError:
    ServicoFeedback = None

try:
    from services.forum import ServicoForum
except ImportError:
    ServicoForum = None

def menu_principal():
    print("=== Fitness App ===")
    print("1. Login")
    print("2. Registrar Usuário")
    print("0. Sair")
    return input("Escolha uma opção: ")

def menu_usuario():
    print("\n--- Menu do Usuário ---")
    print("1. Planos de Treino")
    print("2. Atividades")
    print("3. Nutrição")
    print("4. Metas")
    print("5. Wearable")
    print("6. Social/Desafios")
    print("7. Vídeos (em breve)")
    print("8. Recomendações (em breve)")
    print("9. Feedback (em breve)")
    print("10. Fórum (em breve)")
    print("0. Logout")
    return input("Escolha uma opção: ")

def main():
    auth = ServicoAutenticacao()
    treino = ServicoTreino()
    atividade = ServicoAtividade()
    nutricional = ServicoNutricional()
    meta = ServicoMeta()
    wearable = ServicoWearable()
    social = ServicoSocial()
    video = ServicoVideo() if ServicoVideo else None
    recomendacao = ServicoRecomendacao() if ServicoRecomendacao else None
    feedback = ServicoFeedback() if ServicoFeedback else None
    forum = ServicoForum() if ServicoForum else None

    usuario_logado = None

    while True:
        if not usuario_logado:
            op = menu_principal()
            if op == "1":
                email = input("E-mail: ")
                senha = input("Senha: ")
                usuario_logado = auth.autenticar_usuario(email, senha)
                if usuario_logado:
                    print("Login realizado com sucesso!")
                else:
                    print("Usuário ou senha inválidos.")
            elif op == "2":
                from core.models import Usuario
                nome = input("Nome: ")
                email = input("E-mail: ")
                senha = input("Senha: ")
                genero = input("Gênero: ")
                idade = int(input("Idade: "))
                peso = float(input("Peso (kg): "))
                altura = float(input("Altura (cm): "))
                nivel_atividade = input("Nível de atividade: ")
                objetivo = input("Objetivo: ")
                nivel_experiencia = input("Nível de experiência: ")
                usuario = Usuario(
                    nome, email, senha, genero, idade, peso, altura,
                    nivel_atividade, objetivo, nivel_experiencia
                )
                try:
                    auth.registrar_usuario(usuario)
                    print("Usuário registrado com sucesso!")
                except Exception as e:
                    print(f"Erro ao registrar: {e}")
            elif op == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        else:
            op = menu_usuario()
            if op == "1":
                while True:
                    print("\n--- Planos de Treino ---")
                    print("1. Listar planos")
                    print("2. Criar plano")
                    print("3. Deletar plano")
                    print("0. Voltar")
                    subop = input("Escolha uma opção: ")
                    if subop == "1":
                        planos = treino.listar_planos_usuario(usuario_logado.email)
                        if not planos:
                            print("Nenhum plano cadastrado.")
                        else:
                            for idx, p in enumerate(planos, 1):
                                print(f"{idx}. {p.nome} ({p.nivel})")
                    elif subop == "2":
                        nome = input("Nome do plano: ")
                        objetivo = input("Objetivo: ")
                        nivel = input("Nível: ")
                        exercicios = input("Exercícios (separados por vírgula): ").split(",")
                        treino.criar_plano_personalizado(
                            usuario_email=usuario_logado.email,
                            nome=nome,
                            exercicios=exercicios,
                            objetivo=objetivo,
                            nivel=nivel
                        )
                        print("Plano criado!")
                    elif subop == "3":
                        planos = treino.listar_planos_usuario(usuario_logado.email)
                        for idx, p in enumerate(planos, 1):
                            print(f"{idx}. {p.nome} ({p.nivel})")
                        idx = int(input("Digite o número do plano para deletar: ")) - 1
                        if 0 <= idx < len(planos):
                            treino.deletar_plano(planos[idx].id)
                            print("Plano deletado!")
                        else:
                            print("Índice inválido.")
                    elif subop == "0":
                        break
                    else:
                        print("Opção inválida.")
            elif op == "2":
                while True:
                    print("\n--- Atividades ---")
                    print("1. Listar atividades")
                    print("2. Registrar atividade")
                    print("3. Deletar atividade")
                    print("0. Voltar")
                    subop = input("Escolha uma opção: ")
                    if subop == "1":
                        atividades = atividade.listar_atividades_usuario(usuario_logado.email)
                        if not atividades:
                            print("Nenhuma atividade registrada.")
                        else:
                            for idx, a in enumerate(atividades, 1):
                                print(f"{idx}. {a.tipo} em {a.data} ({a.calorias} kcal)")
                    elif subop == "2":
                        tipo = input("Tipo de atividade: ")
                        data = input("Data (YYYY-MM-DD): ")
                        duracao = input("Duração (min): ")
                        calorias = input("Calorias gastas: ")
                        passos = input("Passos (opcional): ")
                        from core.models import Atividade
                        nova = Atividade(
                            usuario_email=usuario_logado.email,
                            tipo=tipo,
                            data=data,
                            duracao=duracao,
                            calorias=calorias,
                            passos=passos if passos else None
                        )
                        atividade.registrar_atividade(nova)
                        print("Atividade registrada!")
                    elif subop == "3":
                        atividades = atividade.listar_atividades_usuario(usuario_logado.email)
                        for idx, a in enumerate(atividades, 1):
                            print(f"{idx}. {a.tipo} em {a.data}")
                        idx = int(input("Digite o número da atividade para deletar: ")) - 1
                        if 0 <= idx < len(atividades):
                            atividade.deletar_atividade(atividades[idx].id)
                            print("Atividade deletada!")
                        else:
                            print("Índice inválido.")
                    elif subop == "0":
                        break
                    else:
                        print("Opção inválida.")
            elif op == "3":
                while True:
                    print("\n--- Nutrição ---")
                    print("1. Listar registros")
                    print("2. Registrar refeição")
                    print("3. Deletar registro")
                    print("0. Voltar")
                    subop = input("Escolha uma opção: ")
                    if subop == "1":
                        registros = nutricional.listar_registros_usuario(usuario_logado.email)
                        if not registros:
                            print("Nenhum registro encontrado.")
                        else:
                            for idx, r in enumerate(registros, 1):
                                print(f"{idx}. {r.data}: {r.calorias} kcal")
                    elif subop == "2":
                        data = input("Data (YYYY-MM-DD): ")
                        refeicoes = input("Refeições (ex: Peito de frango, Batata-doce): ").split(",")
                        calorias = float(input("Total de calorias: "))
                        proteina = float(input("Proteína (g): "))
                        gordura = float(input("Gordura (g): "))
                        carboidrato = float(input("Carboidrato (g): "))
                        from core.models import RegistroNutricional
                        novo = RegistroNutricional(
                            usuario_email=usuario_logado.email,
                            data=data,
                            refeicoes=refeicoes,
                            calorias=calorias,
                            macros={"proteina": proteina, "gordura": gordura, "carboidrato": carboidrato}
                        )
                        nutricional.registrar_refeicao(novo)
                        print("Refeição registrada!")
                    elif subop == "3":
                        registros = nutricional.listar_registros_usuario(usuario_logado.email)
                        for idx, r in enumerate(registros, 1):
                            print(f"{idx}. {r.data}")
                        idx = int(input("Digite o número do registro para deletar: ")) - 1
                        if 0 <= idx < len(registros):
                            nutricional.deletar_registro(registros[idx].id)
                            print("Registro deletado!")
                        else:
                            print("Índice inválido.")
                    elif subop == "0":
                        break
                    else:
                        print("Opção inválida.")
            elif op == "4":
                while True:
                    print("\n--- Metas ---")
                    print("1. Listar metas")
                    print("2. Criar meta")
                    print("3. Deletar meta")
                    print("0. Voltar")
                    subop = input("Escolha uma opção: ")
                    if subop == "1":
                        metas = meta.listar_metas_usuario(usuario_logado.email)
                        if not metas:
                            print("Nenhuma meta cadastrada.")
                        else:
                            for idx, m in enumerate(metas, 1):
                                status = "Atingida" if m.atingida else "Pendente"
                                print(f"{idx}. {m.tipo}: {m.valor} ({status})")
                    elif subop == "2":
                        tipo = input("Tipo de meta: ")
                        valor = input("Valor/meta: ")
                        data_inicio = input("Data início (YYYY-MM-DD): ")
                        data_fim = input("Data fim (YYYY-MM-DD): ")
                        from core.models import Meta
                        nova = Meta(
                            usuario_email=usuario_logado.email,
                            tipo=tipo,
                            valor=valor,
                            data_inicio=data_inicio,
                            data_fim=data_fim
                        )
                        meta.criar_meta(
                            usuario_email=usuario_logado.email,
                            tipo=tipo,
                            valor=valor,
                            data_inicio=data_inicio,
                            data_fim=data_fim
                        )
                        print("Meta criada!")
                    elif subop == "3":
                        metas = meta.listar_metas_usuario(usuario_logado.email)
                        for idx, m in enumerate(metas, 1):
                            print(f"{idx}. {m.tipo}: {m.valor}")
                        idx = int(input("Digite o número da meta para deletar: ")) - 1
                        if 0 <= idx < len(metas):
                            meta.deletar_meta(metas[idx].id)
                            print("Meta deletada!")
                        else:
                            print("Índice inválido.")
                    elif subop == "0":
                        break
                    else:
                        print("Opção inválida.")
            elif op == "5":
                while True:
                    print("\n--- Wearable ---")
                    print("1. Listar dados")
                    print("2. Registrar dado manual")
                    print("3. Gerar dado aleatório")
                    print("4. Deletar dado")
                    print("0. Voltar")
                    subop = input("Escolha uma opção: ")
                    if subop == "1":
                        dados = wearable.listar_dados_usuario(usuario_logado.email)
                        if not dados:
                            print("Nenhum dado registrado.")
                        else:
                            for idx, d in enumerate(dados, 1):
                                print(f"{idx}. {d.tipo} em {d.data}: {d.valor}")
                    elif subop == "2":
                        tipo = input("Tipo de dado (passos, batimentos, sono): ")
                        valor = input("Valor: ")
                        wearable.registrar_dado_manual(usuario_logado.email, tipo, valor)
                        print("Dado registrado!")
                    elif subop == "3":
                        tipo = input("Tipo de dado (passos, batimentos, sono): ")
                        wearable.gerar_dado_aleatorio(usuario_logado.email, tipo)
                        print("Dado aleatório gerado!")
                    elif subop == "4":
                        dados = wearable.listar_dados_usuario(usuario_logado.email)
                        for idx, d in enumerate(dados, 1):
                            print(f"{idx}. {d.tipo} em {d.data}")
                        idx = int(input("Digite o número do dado para deletar: ")) - 1
                        if 0 <= idx < len(dados):
                            wearable.deletar_dado(dados[idx].id)
                            print("Dado deletado!")
                        else:
                            print("Índice inválido.")
                    elif subop == "0":
                        break
                    else:
                        print("Opção inválida.")
            elif op == "6":
                while True:
                    print("\n--- Social/Desafios ---")
                    print("1. Listar desafios")
                    print("2. Criar desafio")
                    print("3. Participar de desafio")
                    print("4. Deletar desafio")
                    print("0. Voltar")
                    subop = input("Escolha uma opção: ")
                    if subop == "1":
                        desafios = social.listar_desafios()
                        if not desafios:
                            print("Nenhum desafio cadastrado.")
                        else:
                            for idx, d in enumerate(desafios, 1):
                                print(f"{idx}. {d.nome}: {d.descricao}")
                    elif subop == "2":
                        nome = input("Nome do desafio: ")
                        descricao = input("Descrição: ")
                        data_inicio = input("Data início (YYYY-MM-DD): ")
                        data_fim = input("Data fim (YYYY-MM-DD): ")
                        social.criar_desafio(nome, descricao, data_inicio, data_fim)
                        print("Desafio criado!")
                    elif subop == "3":
                        desafios = social.listar_desafios()
                        for idx, d in enumerate(desafios, 1):
                            print(f"{idx}. {d.nome}")
                        idx = int(input("Digite o número do desafio para participar: ")) - 1
                        if 0 <= idx < len(desafios):
                            social.participar_desafio(desafios[idx].id, usuario_logado.email)
                            print("Participação registrada!")
                        else:
                            print("Índice inválido.")
                    elif subop == "4":
                        desafios = social.listar_desafios()
                        for idx, d in enumerate(desafios, 1):
                            print(f"{idx}. {d.nome}")
                        idx = int(input("Digite o número do desafio para deletar: ")) - 1
                        if 0 <= idx < len(desafios):
                            social.deletar_desafio(desafios[idx].id)
                            print("Desafio deletado!")
                        else:
                            print("Índice inválido.")
                    elif subop == "0":
                        break
                    else:
                        print("Opção inválida.")
            elif op == "7":
                print("Funcionalidade de vídeos ainda não implementada.")
            elif op == "8":
                print("Funcionalidade de recomendações ainda não implementada.")
            elif op == "9":
                print("Funcionalidade de feedback ainda não implementada.")
            elif op == "10":
                print("Funcionalidade de fórum ainda não implementada.")
            elif op == "0":
                usuario_logado = None
                print("Logout realizado.")
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()