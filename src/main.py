import flet as ft


def main(page: ft.Page):
    """MVP offline — Guia Prático ML & DL."""

    # Compatibilidade entre versões do Flet
    Icons = getattr(ft, "Icons", None) or getattr(ft, "icons")
    Colors = getattr(ft, "Colors", None) or getattr(ft, "colors")

    def icon(name: str, fallback):
        return getattr(Icons, name, fallback)

    # Configuração mobile
    page.title = "Guia Prático ML & DL"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = Colors.BLUE_GREY_50
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(
        color_scheme_seed=Colors.INDIGO,
        visual_density=ft.VisualDensity.COMPACT,
    )

    # ------------------------------------------------------------------
    # Componentes reutilizáveis
    # ------------------------------------------------------------------
    def md(text: str) -> ft.Markdown:
        return ft.Markdown(
            value=text.strip(),
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            code_theme="atom-one-light",
        )

    def header(title: str, subtitle: str, icon_name: str):
        return ft.Container(
            padding=ft.padding.fromLTRB(20, 22, 20, 14),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[Colors.BLUE_GREY_900, Colors.INDIGO_900],
            ),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=46,
                        height=46,
                        border_radius=14,
                        bgcolor=Colors.with_opacity(0.14, Colors.WHITE),
                        alignment=ft.alignment.center,
                        content=ft.Icon(icon(icon_name, Icons.SCHOOL), color=Colors.INDIGO_100, size=28),
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text(title, size=21, weight=ft.FontWeight.BOLD, color=Colors.WHITE),
                                ft.Text(subtitle, size=13, color=Colors.BLUE_GREY_100),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def phase_title(title: str, subtitle: str):
        return ft.Container(
            padding=ft.padding.fromLTRB(18, 18, 18, 8),
            content=ft.Column(
                spacing=4,
                controls=[
                    ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=Colors.BLUE_GREY_900),
                    ft.Text(subtitle, size=13, color=Colors.BLUE_GREY_600),
                ],
            ),
        )

    def expandable_card(
        title: str,
        summary: str,
        details: str,
        icon_name: str = "INFO_OUTLINE",
    ):
        return ft.Card(
            elevation=1.8,
            margin=ft.margin.symmetric(horizontal=14, vertical=7),
            shape=ft.RoundedRectangleBorder(radius=18),
            content=ft.Container(
                bgcolor=Colors.WHITE,
                border_radius=18,
                padding=ft.padding.symmetric(horizontal=4, vertical=4),
                content=ft.ExpansionTile(
                    initially_expanded=False,
                    title=ft.Text(
                        title,
                        size=15.5,
                        weight=ft.FontWeight.BOLD,
                        color=Colors.INDIGO_700,
                    ),
                    subtitle=ft.Text(summary, size=12.5, color=Colors.BLUE_GREY_600),
                    leading=ft.Container(
                        width=42,
                        height=42,
                        border_radius=14,
                        bgcolor=Colors.INDIGO_50,
                        alignment=ft.alignment.center,
                        content=ft.Icon(icon(icon_name, Icons.INFO_OUTLINE), color=Colors.INDIGO_600, size=24),
                    ),
                    controls=[
                        ft.Container(
                            padding=ft.padding.fromLTRB(18, 0, 18, 16),
                            content=md(details),
                        )
                    ],
                ),
            ),
        )

    def attention_card(text: str):
        return ft.Container(
            margin=ft.margin.symmetric(horizontal=14, vertical=8),
            padding=16,
            border_radius=18,
            bgcolor=Colors.AMBER_100,
            border=ft.border.all(1, Colors.AMBER_300),
            content=ft.Row(
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Icon(icon("WARNING_AMBER_ROUNDED", Icons.WARNING), color=Colors.ORANGE_800, size=26),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text("Atenção", size=15, weight=ft.FontWeight.BOLD, color=Colors.ORANGE_900),
                                md(text),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def tip_card(title: str, text: str):
        return ft.Container(
            margin=ft.margin.symmetric(horizontal=14, vertical=8),
            padding=16,
            border_radius=18,
            bgcolor=Colors.INDIGO_50,
            border=ft.border.all(1, Colors.INDIGO_100),
            content=ft.Row(
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Icon(icon("LIGHTBULB_OUTLINE", Icons.LIGHTBULB), color=Colors.INDIGO_600, size=26),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text(title, size=15, weight=ft.FontWeight.BOLD, color=Colors.INDIGO_700),
                                md(text),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def screen(controls: list[ft.Control]):
        return ft.SafeArea(
            expand=True,
            content=ft.Container(
                width=float("inf"),
                alignment=ft.alignment.top_center,
                content=ft.Container(
                    width=540,
                    padding=ft.padding.only(bottom=88),
                    content=ft.Column(spacing=0, controls=controls),
                ),
            ),
        )

    # ------------------------------------------------------------------
    # Telas
    # ------------------------------------------------------------------
    def preparacao_screen():
        return screen(
            [
                header(
                    "Guia Prático ML & DL",
                    "Aprenda a tomar decisões de ponta a ponta em projetos de dados.",
                    "SCHOOL",
                ),
                phase_title("Fase 1 — Preparação de Dados", "O caminho do dado antes da modelagem."),
                expandable_card(
                    "1. Coleta e Integração",
                    "Centralizar dados brutos em uma base estruturada.",
                    """
A coleta e integração transforma fontes soltas em uma base única de trabalho.

Fontes comuns:

- Planilhas Excel ou CSV.
- Bancos de dados SQL.
- APIs.
- Sistemas internos.

Cuidados práticos:

- Padronizar nomes de colunas.
- Verificar chaves e identificadores.
- Conferir datas, códigos e categorias.
- Criar uma base final em formato de DataFrame.

```text
Planilhas + Banco SQL + API
        ↓
DataFrame analítico
        ↓
Base pronta para limpeza
```
                    """,
                    "DATA_ARRAY",
                ),
                expandable_card(
                    "2. Data Munging — A Faxina",
                    "Limpar imperfeições antes de treinar qualquer modelo.",
                    """
É a etapa de limpeza da base.

O que verificar:

- Registros duplicados.
- Valores nulos.
- Erros de digitação.
- Categorias inconsistentes.
- Outliers que distorcem estatísticas.

Decisões comuns:

- Excluir linhas muito incompletas.
- Imputar valores ausentes.
- Corrigir padrões de escrita.
- Tratar outliers com regra de negócio.

```text
Dado bruto → Dado limpo
```
                    """,
                    "CLEANING_SERVICES",
                ),
                expandable_card(
                    "3. Data Wrangling — A Transformação",
                    "Converter dados limpos em dados modeláveis.",
                    """
Aqui o dado é preparado para o algoritmo.

Transformações comuns:

- Categóricas → One-Hot Encoding.
- Números → padronização ou normalização.
- Datas → tempo de casa, mês, ano, sazonalidade.
- Textos → vetores ou embeddings, quando necessário.

Exemplo:

```text
Cargo = Enfermeiro
Cargo = Técnico
Cargo = Auxiliar

vira

Cargo_Enfermeiro = 1/0
Cargo_Tecnico    = 1/0
Cargo_Auxiliar   = 1/0
```
                    """,
                    "TRANSFORM",
                ),
                expandable_card(
                    "4. Train/Test Split",
                    "Separar treino e teste para medir generalização.",
                    """
A base precisa ser dividida para evitar avaliação enganosa.

Exemplo:

```text
80% treino / 20% teste
```

Uso correto:

- Treino: o modelo aprende os padrões.
- Teste: o modelo é avaliado em dados inéditos.

Risco evitado:

- Overfitting, quando o modelo decora a base histórica e falha em dados novos.

Em séries temporais, a separação deve respeitar o tempo:

```text
Passado → Treino
Futuro  → Teste
```
                    """,
                    "SPLITSCREEN",
                ),
                tip_card(
                    "Dica importante",
                    "Uma boa preparação de dados costuma ter mais impacto no sucesso do modelo do que a escolha do algoritmo em si.",
                ),
            ]
        )

    def modelos_screen():
        return screen(
            [
                header("Escolha do Modelo", "Cada tipo de problema pede uma família diferente de algoritmos.", "PSYCHOLOGY"),
                phase_title("Fase 2 — Escolha do Modelo", "Comece pelo tipo de alvo que será previsto."),
                expandable_card(
                    "Alvo Categórico — Classificação",
                    "Quando a saída esperada é uma classe ou categoria.",
                    """
Use quando o objetivo é prever classes.

Exemplos:

- Churn: sai ou não sai.
- Fraude: sim ou não.
- Risco: baixo, médio ou alto.
- Aprovação: aprovado ou reprovado.

Modelos sugeridos:

- Regressão Logística: baseline simples e interpretável.
- Random Forest: robusta para dados tabulares.
- Gradient Boosting: costuma ter alta performance.

```text
Entrada: histórico e perfil
Saída: classe prevista
```
                    """,
                    "CATEGORY",
                ),
                expandable_card(
                    "Alvo Contínuo — Regressão",
                    "Quando a saída esperada é um número.",
                    """
Use quando o objetivo é prever valores contínuos.

Exemplos:

- Faturamento.
- Preço.
- Tempo de permanência.
- Custo esperado.
- Demanda futura.

Modelos sugeridos:

- Regressão Linear Múltipla: baseline interpretável.
- Random Forest Regressor: captura não linearidade.
- Gradient Boosting Regressor: forte em bases tabulares.

```text
Entrada: variáveis explicativas
Saída: número estimado
```
                    """,
                    "SHOW_CHART",
                ),
                expandable_card(
                    "Sem Alvo — Clusterização / Descoberta",
                    "Quando não existe variável resposta definida.",
                    """
Use quando o objetivo é descobrir padrões ocultos.

Exemplos:

- Criar personas.
- Agrupar clientes.
- Identificar perfis de comportamento.
- Encontrar grupos semelhantes.

Modelos sugeridos:

- K-Means: bom para grupos mais esféricos.
- HDBSCAN: bom para densidade e ruído.
- UMAP: redução de dimensionalidade e visualização.

```text
Entrada: características
Saída: grupos ou mapas de similaridade
```
                    """,
                    "HUB",
                ),
                expandable_card(
                    "Dados Complexos — Deep Learning",
                    "Para grandes volumes e dados não estruturados.",
                    """
Use Deep Learning quando houver volume e complexidade suficientes.

Cenários comuns:

- Imagens.
- Texto.
- Áudio.
- Sequências.
- Dados não estruturados.

Modelos sugeridos:

- MLP: redes densas para dados vetoriais.
- CNNs: imagens e visão computacional.
- Transformers: texto, NLP e linguagem.

```text
Dado complexo → Representação profunda → Predição
```
                    """,
                    "AUTO_AWESOME",
                ),
            ]
        )

    def metricas_screen():
        return screen(
            [
                header("Avaliação de Sucesso", "Métricas para entender se o modelo realmente funciona.", "ANALYTICS"),
                phase_title("Fase 3 — Métricas", "Não avalie o modelo apenas pela acurácia."),
                expandable_card(
                    "Acurácia",
                    "Proporção total de acertos.",
                    """
A acurácia mede quantas previsões o modelo acertou no total.

```text
Acurácia = Total de acertos / Total de casos
```

Cuidado:

Em bases desbalanceadas, a acurácia pode enganar.

Exemplo:

Se 95% dos casos são “Não Fraude”, um modelo que sempre prevê “Não Fraude” pode ter 95% de acurácia e ainda assim ser inútil para encontrar fraudes.
                    """,
                    "FACT_CHECK",
                ),
                expandable_card(
                    "Precisão — Precision",
                    "Confiabilidade do alerta positivo.",
                    """
A precisão responde:

**Quando o modelo disse que era positivo, quantas vezes ele acertou?**

```text
Precisão = VP / (VP + FP)
```

Onde:

- VP = Verdadeiro Positivo.
- FP = Falso Positivo.

Use quando o falso positivo for caro.

Exemplo:

Bloquear uma compra legítima por classificá-la incorretamente como fraude.
                    """,
                    "GPP_GOOD",
                ),
                expandable_card(
                    "Revocação — Recall",
                    "Capacidade de capturar casos positivos reais.",
                    """
O recall responde:

**De todos os casos positivos reais, quantos o modelo encontrou?**

```text
Recall = VP / (VP + FN)
```

Onde:

- VP = Verdadeiro Positivo.
- FN = Falso Negativo.

Use quando deixar passar um caso real for perigoso.

Exemplo:

Não identificar um paciente de alto risco ou uma fraude real.
                    """,
                    "RADAR",
                ),
                expandable_card(
                    "F1-Score",
                    "Equilíbrio entre Precision e Recall.",
                    """
O F1-Score combina precisão e recall em uma única métrica.

```text
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

Interpretação:

- F1 alto indica bom equilíbrio.
- F1 baixo indica que precisão ou recall está ruim.
- Útil quando as classes são desbalanceadas.
                    """,
                    "BALANCE",
                ),
                attention_card(
                    """
Em problemas reais com classes de tamanhos diferentes, calcule o **F1-Score com média ponderada**, também chamado de **weighted average**.

Isso evita que a classe majoritária esconda o mau desempenho nas classes menores.

```text
Preferir: F1 weighted average
Evitar depender apenas de: acurácia simples
```
                    """
                ),
            ]
        )

    # ------------------------------------------------------------------
    # Navegação inferior
    # ------------------------------------------------------------------
    def render(index: int):
        page.controls.clear()
        page.navigation_bar.selected_index = index

        if index == 0:
            page.add(preparacao_screen())
        elif index == 1:
            page.add(modelos_screen())
        else:
            page.add(metricas_screen())

        page.update()

    def on_nav_change(e):
        render(e.control.selected_index)

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        bgcolor=Colors.WHITE,
        elevation=8,
        indicator_color=Colors.INDIGO_100,
        destinations=[
            ft.NavigationBarDestination(
                icon=icon("DATA_EXPLORATION", Icons.DATA_OBJECT),
                selected_icon=icon("DATA_EXPLORATION", Icons.DATA_OBJECT),
                label="Preparação",
            ),
            ft.NavigationBarDestination(
                icon=icon("PSYCHOLOGY", Icons.LIGHTBULB),
                selected_icon=icon("PSYCHOLOGY", Icons.LIGHTBULB),
                label="Modelos",
            ),
            ft.NavigationBarDestination(
                icon=icon("ANALYTICS", Icons.QUERY_STATS),
                selected_icon=icon("ANALYTICS", Icons.QUERY_STATS),
                label="Métricas",
            ),
        ],
    )

    render(0)


if __name__ == "__main__":
    ft.app(target=main)
